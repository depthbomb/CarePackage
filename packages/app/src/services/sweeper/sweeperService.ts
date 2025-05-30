import { join } from 'node:path';
import { IpcChannel } from 'shared';
import { DOWNLOAD_DIR } from '~/constants';
import { IpcService } from '~/services/ipc';
import { WindowService } from '~/services/window';
import { inject, injectable } from '@needle-di/core';
import { LifecycleService } from '~/services/lifecycle';
import { stat, unlink, readdir } from 'node:fs/promises';
import type { IBootstrappable } from '~/common/IBootstrappable';

@injectable()
export class SweeperService implements IBootstrappable {
	private readonly interval: NodeJS.Timeout;

	public constructor(
		private readonly lifecycle = inject(LifecycleService),
		private readonly window    = inject(WindowService),
		private readonly ipc       = inject(IpcService),
	) {
		this.interval = setInterval(async () => {
			const stats = await this.calculateDownloadsSize();
			this.window.emitMain(IpcChannel.Sweeper_DownloadsStats, stats);
		}, 1_500);
	}

	public async bootstrap() {
		this.ipc.registerHandler(IpcChannel.Sweeper_CalculateDownloadsSize, async () => await this.calculateDownloadsSize());
		this.ipc.registerHandler(IpcChannel.Sweeper_PerformSweep, async () => await this.sweepDownloads());

		this.lifecycle.events.on('shutdown', () => clearInterval(this.interval));
	}

	public async sweepDownloads() {
		let sweptFiles = 0;

		const files = await readdir(DOWNLOAD_DIR, { withFileTypes: true });
		for (const file of files) {
			if (!file.isFile()) {
				continue;
			}

			await unlink(
				join(DOWNLOAD_DIR, file.name)
			);

			sweptFiles++;
		}

		return sweptFiles;
	}

	public async calculateDownloadsSize() {
		let totalSize  = 0;
		let totalFiles = 0;

		const files = await readdir(DOWNLOAD_DIR, { withFileTypes: true });
		for (const file of files) {
			if (!file.isFile()) {
				continue;
			}

			const filePath = join(DOWNLOAD_DIR, file.name);
			const stats    = await stat(filePath);

			totalSize += stats.size;
			totalFiles++;
		}

		return [totalFiles, totalSize] as const;
	}
}
