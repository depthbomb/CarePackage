import mitt from 'mitt';
import { x } from 'tinyexec';
import { timeout } from '~/common/async';
import { randomUUID } from 'node:crypto';
import { getExtraFilePath } from '~/utils';
import { HttpService } from '~/services/http';
import { findFreePort } from '~/common/ports';
import { dirname, basename } from 'node:path';
import { IpcChannel, SettingsKey } from 'shared';
import { WindowService } from '~/services/window';
import { inject, injectable } from '@needle-di/core';
import { SettingsService } from '~/services/settings';
import { LifecycleService } from '~/services/lifecycle';
import { USER_AGENT, BROWSER_USER_AGENT } from '~/constants';
import type { Maybe } from 'shared';
import type { HttpClient } from '~/services/http';
import type { IBootstrappable } from '~/common/IBootstrappable';

@injectable()
export class Aria2Service implements IBootstrappable {
	public readonly events = mitt<{
		downloadStarted: string;
		downloadError: string;
		downloadCompleted: string;
	}>();

	private id: number   = 1;
	private port: number = 6800;
	private ws: Maybe<WebSocket>;
	private proc: Maybe<ReturnType<typeof x>>;

	private readonly client: HttpClient;
	private readonly rpcSecret: string;
	private readonly binaryPath: string;
	private readonly maxDownloadLimitPattern: RegExp;

	public constructor(
		private readonly lifecycle = inject(LifecycleService),
		private readonly window    = inject(WindowService),
		private readonly settings  = inject(SettingsService),
		private readonly http      = inject(HttpService),
	) {
		this.client                  = this.http.getClient('Aria2cJSON-RPC', { userAgent: USER_AGENT});
		this.rpcSecret               = randomUUID();
		this.binaryPath              = getExtraFilePath('bin/aria2c.exe');
		this.maxDownloadLimitPattern = /^(\d+)([A-Z]*)$/;
	}

	public async bootstrap() {
		this.lifecycle.events.on('shutdown', async () => {
			if (this.proc && (!this.proc.killed || !this.proc.aborted)) {
				await this.callMethod('aria2.forceShutdown');
			}

			this.stopProcess();
		});

		// Modify the download limit before saving it to valid it
		this.settings.registerSetHook<string>(SettingsKey.Aria2_MaxDownloadLimit, (value) => {
			value = value.trim().toUpperCase();
			if (value === '0B' || value.length === 0) {
				return '0';
			}

			const match = value.match(this.maxDownloadLimitPattern);
			if (!match) {
				return '0';
			}

			const number = match[1];
			const unit   = match[2];
			if (isNaN(Number(number)) || Number(number) < 0) {
				return '0';
			}

			if (unit === '' || unit === 'K' || unit === 'M') {
				return `${number}${unit}`;
			}

			if (unit === 'B') {
				return number;
			}

			return number;
		});
	}

	public async startProcess(signal: AbortSignal) {
		if (!this.proc?.killed || !this.proc?.aborted) {
			await this.stopProcess();
		}

		this.port = await findFreePort(this.port, 5, 5_000);
		if (this.port === 0) {
			throw new Error('Unable to find free port for aria2c');
		}

		const maxConcurrentDownloads = this.settings.get<number>(SettingsKey.Aria2_MaxConcurrentDownloads);
		const maxDownloadLimit       = this.settings.get<string>(SettingsKey.Aria2_MaxDownloadLimit);

		this.proc = x(this.binaryPath, [
			'--enable-rpc=true',
			`--rpc-secret=${this.rpcSecret}`,
			`--rpc-listen-port=${this.port}`,
			'--rpc-listen-all=false',
			'--rpc-allow-origin-all=true',
			'--auto-file-renaming=false',
			'--allow-overwrite=true',
			'--always-resume=false',
			`--user-agent=${BROWSER_USER_AGENT}`,
			'--max-connection-per-server=1',
			'--file-allocation=none',
			//
			`--max-concurrent-downloads=${maxConcurrentDownloads}`,
			`--max-overall-download-limit=${maxDownloadLimit}`,
		], {
			signal,
			nodeOptions: { detached: true }
		});

		if (import.meta.env.DEV) {
			this.consumeOutput(this.proc);
		}

		await this.connectToWs();

		this.window.emitMain(IpcChannel.Aria2_Ready);
	}

	public async stopProcess() {
		if (this.proc?.killed) {
			return;
		}

		this.proc?.kill();

		return new Promise<void>(res => {
			setInterval(() => {
				if (!this.proc || this.proc.killed || this.proc.aborted) {
					res();
				}
			}, 100);
		});
	}

	public async addUri(uri: string[], destination: string, gid: string) {
		const destinationFolder = dirname(destination);
		const destinationFile   = basename(destination);
		await this.callMethod<string>('aria2.addUri', [
			uri,
			{
				gid,
				dir: destinationFolder,
				out: destinationFile
			}
		]);

		return gid;
	}

	public async forcePauseAll() {
		return this.callMethod('aria2.forcePauseAll');
	}

	public async remove(gid: string) {
		return this.callMethod('aria2.remove', [gid]);
	}

	public async forceRemove(gid: string) {
		return this.callMethod('aria2.forceRemove', [gid]);
	}

	public async purgeDownloadResult() {
		return this.callMethod('aria2.purgeDownloadResult');
	}

	public async changeGlobalOption(options: Record<string, string | number | boolean>) {
		return this.callMethod('aria2.changeGlobalOption', [options]);
	}

	public async multicall(methods: Array<{ methodName: string; params: unknown[] }>) {
		return this.callMethod('system.multicall', [methods]);
	}

	private async callMethod<T>(method: string, params: unknown[] = []) {
		if (!this.proc || this.proc?.killed || this.proc?.aborted) {
			return null;
		}

		try {
			const payload = {
				jsonrpc: '2.0',
				id: `q${this.id++}`,
				method,
				params: [`token:${this.rpcSecret}`, ...params]
			};

			const res = await this.client.send(`http://localhost:${this.port}/jsonrpc`, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(payload)
			});

			const data = await res.json();

			return (data as any).result as T;
		} catch (err) {
			console.error(err);
			throw err;
		}
	}

	private async connectToWs() {
		let connected = false;
		while (!connected) {
			await timeout(500);

			try {
				const res = await this.callMethod<object>('aria2.getVersion');
				connected = !!res && 'version' in res;
			} catch {}
		}

		this.ws = new WebSocket(`ws://localhost:${this.port}/jsonrpc`);
		if (import.meta.env.DEV) {
			this.ws.addEventListener('open', () => console.log('Connected to aria2 websocket'));
		}
		this.ws.addEventListener('message', e => {
			const data = JSON.parse(e.data) as { method: string; params: any[]; };
			switch (data.method) {
				case 'aria2.onDownloadStart':
					this.events.emit('downloadStarted', data.params[0].gid);
					break;
				case 'aria2.onDownloadError':
					this.events.emit('downloadError', data.params[0].gid);
					break;
				case 'aria2.onDownloadComplete':
					this.events.emit('downloadCompleted', data.params[0].gid);
					break;
			}
		});
	}

	private async consumeOutput(iterator: AsyncIterable<string>) {
		for await (let line of iterator) {
			line = line.trim();
			if (line.length > 0) {
				console.debug(line);
			}
		}
	}
}
