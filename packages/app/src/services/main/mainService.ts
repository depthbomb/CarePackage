import { IpcChannel } from 'shared';
import { IpcService } from '~/services/ipc';
import { app, shell, dialog } from 'electron';
import { ThemeService } from '~/services/theme';
import { Aria2Service } from '~/services/aria2';
import { WindowService } from '~/services/window';
import { NativeService } from '~/services/native';
import { StartupService } from '~/services/startup';
import { SweeperService } from '~/services/sweeper';
import { UpdaterService } from '~/services/updater';
import { inject, injectable } from '@needle-di/core';
import { SettingsService } from '~/services/settings';
import { FirstRunService } from '~/services/firstRun';
import { SoftwareService } from '~/services/software';
import { MainWindowService } from '~/services/mainWindow';
import { LifecyclePhase, LifecycleService } from '~/services/lifecycle';
import type { MessageBoxOptions } from 'electron';

@injectable()
export class MainService {
	public constructor(
		private readonly lifecycle  = inject(LifecycleService),
		private readonly startup    = inject(StartupService),
		private readonly ipc        = inject(IpcService),
		private readonly window     = inject(WindowService),
		private readonly theme      = inject(ThemeService),
		private readonly native     = inject(NativeService),
		private readonly settings   = inject(SettingsService),
		private readonly firstRun   = inject(FirstRunService),
		private readonly mainWindow = inject(MainWindowService),
		private readonly software   = inject(SoftwareService),
		private readonly sweeper    = inject(SweeperService),
		private readonly updater    = inject(UpdaterService),
		private readonly aria2      = inject(Aria2Service),
	) {}

	public async boot() {
		if (import.meta.env.PROD) {
			await this.firstRun.performFirstRunTasks();
		}

		await this.startup.performStartupTasks();

		await Promise.allSettled([
			this.lifecycle.bootstrap(),
			this.theme.bootstrap(),
			this.settings.bootstrap(),
			this.mainWindow.bootstrap(),
			this.software.bootstrap(),
			this.sweeper.bootstrap(),
			this.updater.bootstrap(),
			this.aria2.bootstrap(),
		]);

		this.lifecycle.phase = LifecyclePhase.Ready;

		this.ipc.registerHandler(
			IpcChannel.ShowMessageBox,
			async (_, options: MessageBoxOptions) => await dialog.showMessageBox(this.window.getMainWindow()!, options)
		);
		this.ipc.registerHandler(IpcChannel.IsElevated, () => this.native.isElevated());
		this.ipc.registerHandler(
			IpcChannel.RestartAsElevated,
			(_, softwareKeys: string[]) => {
				this.mainWindow.browserWindow?.hide();
				this.native.runAsAdmin(app.getPath('exe'), [`--software ${softwareKeys.join(',')}`]);
				app.quit();
			}
		);
		this.ipc.registerHandler(IpcChannel.OpenExternalUrl, (_, url: string) => shell.openExternal(url));
	}
}
