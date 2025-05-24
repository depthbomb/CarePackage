import { join } from 'node:path';
import { IpcChannel } from 'shared';
import { DOWNLOAD_DIR } from '~/constants';
import { IpcService } from '~/services/ipc';
import { inject, injectable } from '@needle-di/core';
import { stat, unlink, readdir } from 'node:fs/promises';
import type { IBootstrappable } from '~/common/IBootstrappable';

@injectable()
export class SweeperService implements IBootstrappable {
	public constructor(
		private readonly ipc = inject(IpcService),
	) {}

	public async bootstrap() {
		this.ipc.registerHandler(IpcChannel.Sweeper_CalculateDownloadsSize, async () => await this.calculateDownloadsSize());
		this.ipc.registerHandler(IpcChannel.Sweeper_PerformSweep, async () => await this.sweepDownloads());
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
