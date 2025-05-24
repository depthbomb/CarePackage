export enum SettingsKey {
	// UI
	UI_ShowCategoryBadges = 'ui_showCategoryBadges',
	// Aria2
	Aria2_MaxTries                = 'aria2_maxTries',
	Aria2_MaxConcurrentDownloads  = 'aria2_maxConcurrentDownloads',
	Aria2_MaxDownloadLimit        = 'aria2_maxDownloadLimit',
	Aria2_MaxConnectionsPerServer = 'aria2_maxConnectionsPerServer',
}

export const SettingsKeys = Object.values(SettingsKey);

export function isSettingsKey(input: string, ...keys: SettingsKey[]): boolean {
	return keys.includes(input as SettingsKey);
}
