import { SettingsKey } from 'shared';
import { inject, injectable } from '@needle-di/core';
import { SettingsService } from '~/services/settings';

@injectable()
export class StartupService {
	public constructor(
		private readonly settings = inject(SettingsService)
	) {}

	public async performStartupTasks() {
		await this.applyDefaultSettings();
	}

	private async applyDefaultSettings() {
		await this.settings.setDefault(SettingsKey.UI_ShowCategoryBadges, true);
		await this.settings.setDefault(SettingsKey.Aria2_MaxTries, 5);
		await this.settings.setDefault(SettingsKey.Aria2_MaxConcurrentDownloads, 5);
		await this.settings.setDefault(SettingsKey.Aria2_MaxDownloadLimit, '0', { skipHooks: true });
	}
}
