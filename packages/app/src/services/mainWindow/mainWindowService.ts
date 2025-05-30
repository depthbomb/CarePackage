import { join } from 'node:path';
import { IpcChannel } from 'shared';
import { CliService } from '~/services/cli';
import { IpcService } from '~/services/ipc';
import { WindowService } from '~/services/window';
import { inject, injectable } from '@needle-di/core';
import { SoftwareService } from '~/services/software';
import { net, Menu, shell, protocol } from 'electron';
import { fileExists, getExtraResourcePath } from '~/utils';
import { PRELOAD_PATH, EXTERNAL_HOSTS_WHITELIST } from '~/constants';
import type { Maybe } from 'shared';
import type { BrowserWindow } from 'electron';
import type { IBootstrappable } from '~/common/IBootstrappable';

@injectable()
export class MainWindowService implements IBootstrappable {
	private mainWindow: Maybe<BrowserWindow>;

	private readonly softwareMenuCache: Map<string, Menu>;

	public constructor(
		private readonly cli      = inject(CliService),
		private readonly ipc      = inject(IpcService),
		private readonly window   = inject(WindowService),
		private readonly software = inject(SoftwareService),
	) {
		this.softwareMenuCache = new Map();
	}

	public get browserWindow() {
		return this.mainWindow;
	}

	public async bootstrap() {
		this.mainWindow = this.window.createMainWindow({
			url: this.window.resolveRendererHTML(`index.html?software=${this.cli.flags.software}`),
			browserWindowOptions: {
				show: false,
				width: 1000,
				minWidth: 1000,
				height: 600,
				minHeight: 600,
				frame: false,
				backgroundColor: '#18181b',
				roundedCorners: true,
				webPreferences: {
					spellcheck: false,
					enableWebSQL: false,
					nodeIntegration: true,
					devTools: import.meta.env.DEV,
					preload: PRELOAD_PATH,
				}
			},
			onReadyToShow: () => {
				this.mainWindow!.show();
				this.mainWindow!.moveTop();
				this.mainWindow!.focus();
			},
		});

		this.mainWindow.webContents.setWindowOpenHandler(({ url }) => {
			const requestedUrl = new URL(url);
			if (EXTERNAL_HOSTS_WHITELIST.includes(requestedUrl.host)) {
				shell.openExternal(url);
			}

			return { action: 'deny' };
		});

		protocol.handle('software-icon', async ({ url }) => {
			let iconPath = getExtraResourcePath(
				join('software-icons', url.replace('software-icon://', ''))
			);

			const exists = await fileExists(iconPath);
			if (!exists) {
				iconPath = getExtraResourcePath(
					join('software-icons', 'generic.png')
				);
			}

			return net.fetch(`file://${iconPath}`);
		});

		this.mainWindow.on('focus', () => {
			this.mainWindow?.flashFrame(false);
			this.window.emitMain(IpcChannel.MainWindow_Focused);
		});
		this.mainWindow.on('blur',       () => this.window.emitMain(IpcChannel.MainWindow_Blurred));
		this.mainWindow.on('maximize',   () => this.window.emitMain(IpcChannel.MainWindow_Maximized));
		this.mainWindow.on('unmaximize', () => this.window.emitMain(IpcChannel.MainWindow_Restored));
		this.mainWindow.on('restore',    () => this.window.emitMain(IpcChannel.MainWindow_Restored))

		this.ipc.registerHandler(IpcChannel.MainWindow_Minimize, () => this.mainWindow?.minimize());
		this.ipc.registerHandler(IpcChannel.MainWindow_Maximize, () => this.mainWindow?.maximize());
		this.ipc.registerHandler(IpcChannel.MainWindow_Restore,  () => this.mainWindow?.restore());
		this.ipc.registerHandler(IpcChannel.MainWindow_Close,    () => this.mainWindow?.close());
		this.ipc.registerHandler(IpcChannel.Software_ShowContextMenu, (_, key: string) => {
			const software = this.software.definitions.values().find(sw => sw.key === key);
			if (!software) {
				return;
			}

			let menu: Menu;
			if (this.softwareMenuCache.has(software.key)) {
				menu = this.softwareMenuCache.get(software.key)!;
			} else {
				menu = Menu.buildFromTemplate([
					{
						label: 'Visit homepage',
						async click() {
							await shell.openExternal(software.homepage);
						}
					}
				]);

				this.softwareMenuCache.set(software.key, menu);
			}

			menu.popup({ window: this.mainWindow });
		});
	}
}
