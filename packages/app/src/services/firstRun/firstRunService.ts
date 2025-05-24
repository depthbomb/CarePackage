import { join } from 'node:path';
import { app, dialog } from 'electron';
import { touch, fileExists } from '~/utils';
import { injectable } from '@needle-di/core';

@injectable()
export class FirstRunService {
	private readonly firstRunFilePath: string;

	public constructor() {
		this.firstRunFilePath = join(app.getPath('userData'), '.first-run');
	}

	public async performFirstRunTasks() {
		const isFirstRun = await this.isFirstRun();
		if (!isFirstRun) {
			return;
		}

		await this.showDisclaimerDialog();
	}

	public async isFirstRun(dry = false) {
		const exists = await fileExists(this.firstRunFilePath);

		if (!dry) {
			await touch(this.firstRunFilePath);
		}

		return !exists;
	}

	private async showDisclaimerDialog() {
		await dialog.showMessageBox({
			type: 'info',
			title: 'Disclaimer',
			message: 'CarePackage is an independent, open-source project and is not affiliated with, endorsed by, or associated with the software it manages. All trademarks and software names are the property of their respective owners.'
		});
	}
}
