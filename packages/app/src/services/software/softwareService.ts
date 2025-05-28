import { join } from 'node:path';
import { timeout } from '~/common/async';
import { createHash } from 'node:crypto';
import { CliService } from '~/services/cli';
import { IpcService } from '~/services/ipc';
import { app, shell, dialog } from 'electron';
import { Aria2Service } from '~/services/aria2';
import { createDir, fileExists } from '~/utils';
import { NativeService } from '~/services/native';
import { WindowService } from '~/services/window';
import { unlink, writeFile } from 'node:fs/promises';
import { inject, injectable } from '@needle-di/core';
import { LifecycleService } from '~/services/lifecycle';
import { InstallationService } from '~/services/installation';
import { DOWNLOAD_DIR, MONOREPO_ROOT_PATH } from '~/constants';
import { IpcChannel, SoftwareCategory, PostOperationAction } from 'shared';
import type { IBootstrappable } from '~/common/IBootstrappable';
import type { DownloadOptions, ISoftwareDefinition } from 'shared';

@injectable()
export class SoftwareService implements IBootstrappable {
	public readonly definitions: Set<ISoftwareDefinition>;

	private abort                 = new AbortController();
	private aborted               = false;
	private working               = false;
	private downloadProgress      = 0;
	private downloadProgressTotal = 100;

	private readonly urlCache: Map<string, string>;
	private readonly erroredSoftware: Set<ISoftwareDefinition>;
	private readonly gidToSoftwareMap: Map<string, ISoftwareDefinition>;

	public constructor(
		private readonly cli          = inject(CliService),
		private readonly lifecycle    = inject(LifecycleService),
		private readonly ipc          = inject(IpcService),
		private readonly window       = inject(WindowService),
		private readonly native       = inject(NativeService),
		private readonly aria2        = inject(Aria2Service),
		private readonly installation = inject(InstallationService),
	) {
		this.definitions      = new Set();
		this.urlCache         = new Map();
		this.gidToSoftwareMap = new Map();
		this.erroredSoftware  = new Set();

		const modules = import.meta.glob('./definitions/*.ts');
		for (const path in modules) {
			modules[path]().then((mod: any) => {
				const defClass   = mod.default as new() => ISoftwareDefinition;
				const definition = new defClass();
				if (this.definitions.has(definition)) {
					return;
				}

				this.definitions.add(definition);
			});
		}
	}

	public async bootstrap() {
		await createDir(DOWNLOAD_DIR);

		this.lifecycle.events.on('shutdown', () => this.cancelDownload());

		this.aria2.events.on('downloadStarted', gid => {
			if (this.aborted) {
				return;
			}

			const software = this.gidToSoftwareMap.get(gid)!;
			this.window.emitMain(IpcChannel.Software_DownloadStarted, software);
		});
		this.aria2.events.on('downloadCompleted', gid => {
			if (this.aborted) {
				return;
			}

			const software = this.gidToSoftwareMap.get(gid)!;
			this.window.emitMain(IpcChannel.Software_DownloadCompleted, software);
			this.gidToSoftwareMap.delete(gid);

			this.downloadProgress++;
			this.window.getMainWindow()?.setProgressBar(this.downloadProgressTotal === 0 ? 0 : this.downloadProgress / this.downloadProgressTotal, { mode: 'normal' });
		});
		this.aria2.events.on('downloadError', gid => {
			if (this.aborted) {
				return;
			}

			const software = this.gidToSoftwareMap.get(gid)!;
			this.window.emitMain(IpcChannel.Software_DownloadError, software);
			this.erroredSoftware.add(software);
			this.gidToSoftwareMap.delete(gid);
		});

		this.ipc.registerHandler(IpcChannel.Software_GetDefinitions, () => this.definitions.values().toArray());
		this.ipc.registerHandler(IpcChannel.Software_GetPreviousSelection, () => {
			if (this.cli.flags.software) {
				return this.cli.flags.software.split(',');
			}

			return [];
		});
		this.ipc.registerHandler(IpcChannel.Software_StartDownload, async (_, keys: string[], options: DownloadOptions) => await this.downloadSoftwareFromKeys(keys, options));
		this.ipc.registerHandler(IpcChannel.Software_CancelDownload, () => this.cancelDownload());

		/**
		 * Generate the software table in development mode which will be committed
		 */
		if (import.meta.env.DEV) {
			await this.generateTableMarkdown();
		}
	}

	public async downloadSoftwareFromKeys(keys: string[], options: DownloadOptions) {
		if (this.working) {
			return;
		}

		const softwares = this.definitions.values().filter(d => keys.includes(d.key)).toArray();
		if (softwares.length === 0) {
			throw new Error();
		}

		this.abort                 = new AbortController();
		this.aborted               = false;
		this.working               = true;
		this.downloadProgress      = 0;
		this.downloadProgressTotal = softwares.length;

		this.gidToSoftwareMap.clear();
		this.erroredSoftware.clear();

		await this.aria2.startProcess(this.abort.signal);

		for (const software of softwares) {
			if (this.aborted) {
				break;
			}

			this.window.emitMain(IpcChannel.Software_ResolvingDownloadUrl, software);

			let downloadUrl: string;
			if (this.urlCache.has(software.key)) {
				downloadUrl = this.urlCache.get(software.key)!;
			} else {
				const resolvedDownloadUrl = await software.resolveDownloadUrl();
				if (resolvedDownloadUrl.isOk()) {
					downloadUrl = resolvedDownloadUrl.value;
				} else {
					this.window.emitMain(IpcChannel.Software_UrlResolveError, software, resolvedDownloadUrl.error);
					this.erroredSoftware.add(software);
					continue;
				}
			}

			if (software.shouldCacheUrl) {
				this.urlCache.set(software.key, downloadUrl);
			}

			this.window.emitMain(IpcChannel.Software_ResolvedDownloadUrl, software);

			const downloadPath = join(DOWNLOAD_DIR, software.downloadName);

			try {
				// Manually create the GID because sometimes the download starts before we get the
				// GID to add to gidToSoftwareMap
				const gid = createHash('md5').update(Math.random().toString()).digest('hex').substring(0, 16);

				this.gidToSoftwareMap.set(gid, software);

				await this.aria2.addUri([downloadUrl], downloadPath, gid);
			} catch (err) {
				this.window.emitMain(IpcChannel.Software_DownloadError, software, (err as Error).message);
				this.erroredSoftware.add(software);
				continue;
			}
		}

		// Poll until downloads have finished
		while (this.gidToSoftwareMap.keys().toArray().length > 0 && !this.aborted) {
			await timeout(100);
		}

		await this.aria2.stopProcess();

		if (this.aborted) {
			this.working = false;
			this.window.emitMain(IpcChannel.Software_Aborted);
			this.window.getMainWindow()?.setProgressBar(0, { mode: 'none' });
			return;
		}

		const hasErrors = this.erroredSoftware.size > 0;
		if (hasErrors) {
			this.window.getMainWindow()?.setProgressBar(1, { mode: 'error' });

			await dialog.showMessageBox({
				type: 'error',
				title: 'Error',
				message: 'Some software failed to resolve to a valid download URL or failed to download entirely.\nPlease try again later. If the issue persists then please submit an issue on GitHub'
			});
		}

		this.window.emitMain(IpcChannel.Software_DownloadsFinished);

		if (!options.skipInstallation && !this.aborted) {
			this.window.getMainWindow()?.setProgressBar(1, { mode: 'indeterminate' });

			for (const software of softwares.filter(sw => !sw.isArchive)) {
				if (this.aborted) {
					break;
				}

				const installerPath = join(DOWNLOAD_DIR, software.downloadName);

				this.window.emitMain(IpcChannel.Software_RunningExecutable, software);

				const code = await this.installation.runExecutable(installerPath, options.installSilently);

				this.window.emitMain(IpcChannel.Software_ExecutableExited, software, code);

				if (code === 0 && options.cleanupAfterInstall) {
					await unlink(installerPath);
				}
			}
		}

		if (options.openDownloadDir && !this.aborted) {
			await shell.openPath(DOWNLOAD_DIR);
		}

		if (options.postOperationAction > 0 && !this.aborted) {
			this.performPostOperationAction(options.postOperationAction);
		}

		this.window.getMainWindow()?.setProgressBar(0, { mode: 'none' });
		this.window.getMainWindow()?.flashFrame(true);
		this.window.emitMain(IpcChannel.Software_AllDone, hasErrors);
		this.working = false;
	}

	public async cancelDownload() {
		if (this.aborted) {
			return;
		}

		this.aborted = true;
		this.abort.abort();
		this.gidToSoftwareMap.clear();

		await this.aria2.stopProcess();
	}

	private performPostOperationAction(action: PostOperationAction) {
		switch (action) {
			case PostOperationAction.Quit:
				app.quit();
				break;
			case PostOperationAction.LogOut:
				this.native.logOut();
				app.quit();
				break;
			case PostOperationAction.LockSystem:
				this.native.lock();
				break;
			case PostOperationAction.RestartSystem:
				this.native.scheduleShutdown(30, 'CarePackage has scheduled a system restart in 30 seconds.', true, true);
				app.quit();
				break;
			case PostOperationAction.ShutDownSystem:
				this.native.scheduleShutdown(60, 'CarePackage has scheduled a system shutdown in 1 minute.', false, true);
				app.quit();
				break;
		}
	}

	private async generateTableMarkdown() {
		const markdownPath = join(MONOREPO_ROOT_PATH, 'SOFTWARE.md');
		const exists       = await fileExists(markdownPath);
		if (exists) {
			await unlink(markdownPath);
		}

		const markdown = ['# All Software'];

		for (const category of Object.values(SoftwareCategory)) {
			const categorySoftware = Array.from(this.definitions.values().filter(sw => sw.category.includes(category)));
			markdown.push(
				`\n## ${category}`,
				'\n|  | Name | Is Archive? | Requires Admin? | Additional Categories |',
				'| :-: | --- | :-: | :-: | :-: |'
			);

			for (const sw of categorySoftware) {
				const icon       = `./static/extra/software-icons/${sw.icon}`;
				const isArchive  = sw.isArchive ? '✔' : '❌';
				const isUac      = sw.requiresAdmin ? '✔' : '❌';
				const categories = sw.category.filter(c => c !== category).join(', ');

				markdown.push(
					`| ![${sw.name}](${icon} "${sw.name}") | [${sw.name}](${sw.homepage}) | ${isArchive} | ${isUac} | ${categories.length ? categories : 'None'}`
				);
			}

			markdown.push('\n---');
		}

		await writeFile(markdownPath, markdown.join('\n'), 'utf8');
	}
}
