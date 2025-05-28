export enum IpcChannel {
	ShowMessageBox    = 'show-message-box',
	IsElevated        = 'is-elevated',
	RestartAsElevated = 'restart-as-elevated',
	OpenExternalUrl   = 'open-external-url',
	// Main Window channels
	MainWindow_Minimize  = 'main-window:minimize',
	MainWindow_Maximize  = 'main-window:maximize',
	MainWindow_Restore   = 'main-window:restore',
	MainWindow_Minimized = 'main-window:minimized',
	MainWindow_Maximized = 'main-window:maximized',
	MainWindow_Restored  = 'main-window:restored',
	MainWindow_Close     = 'main-window:close',
	// Settings channels
	Settings_Get     = 'settings:get',
	Settings_Set     = 'settings:set',
	Settings_Reset   = 'settings:reset',
	Settings_Changed = 'settings:changed',
	// Aria2 channels
	Aria2_Ready = 'aria2:ready',
	// Software channels
	Software_GetDefinitions       = 'software:get-definitions',
	Software_GetPreviousSelection = 'software:get-previous-selection',
	Software_ShowContextMenu      = 'software:show-context-menu',
	Software_ResolvingDownloadUrl = 'software:resolving-download-url',
	Software_UrlResolveError      = 'software:url-resolve-error',
	Software_ResolvedDownloadUrl  = 'software:resolved-download-url',
	Software_DownloadStarted      = 'software:download-started',
	Software_DownloadError        = 'software:download-error',
	Software_DownloadCompleted    = 'software:download-completed',
	Software_StartDownload        = 'software:start-download',
	Software_CancelDownload       = 'software:cancel-download',
	Software_DownloadsFinished    = 'software:downloads-finished',
	Software_RunningExecutable    = 'software:running-executable',
	Software_ExecutableExited     = 'software:executable-exited',
	Software_Aborted              = 'software:aborted',
	Software_AllDone              = 'software:all-done',
	// Sweeper channels
	Sweeper_CalculateDownloadsSize = 'sweeper:calculate-downloads-size',
	Sweeper_PerformSweep           = 'sweeper:perform-sweep',
	// Updater channels
	Updater_Outdated           = 'updater:outdated',
	Updater_CheckingForUpdates = 'updater:checking-for-updates',
}

export const IpcChannels = Object.values(IpcChannel);
