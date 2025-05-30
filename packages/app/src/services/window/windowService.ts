import mitt from 'mitt';
import { join } from 'node:path';
import { ROOT_PATH } from '~/constants';
import { injectable } from '@needle-di/core';
import { app, BrowserWindow } from 'electron';
import { DEV_PORT, IpcChannel } from 'shared';
import type { Awaitable } from 'shared';
import type { AboutPanelOptionsOptions, BrowserWindowConstructorOptions } from 'electron';

type CreateWindowOptions = {
	/**
	 * URL or local path to contents to load into the window.
	 */
	url: string;
	/**
	 * {@link BrowserWindowConstructorOptions}
	 */
	browserWindowOptions: BrowserWindowConstructorOptions;
	/**
	 * The function to call when the window is ready to be shown.
	 */
	onReadyToShow?: () => Awaitable<void>;
};
type CreateMainWindowOptions = Omit<CreateWindowOptions, 'name'>;

@injectable()
export class WindowService {
	public readonly events = mitt<{ windowCreated: BrowserWindow; windowDestroyed: BrowserWindow; }>();
	public readonly windows: Map<string, BrowserWindow>;

	private readonly mainWindowName = 'main' as const;

	public constructor() {
		this.windows = new Map();
	}

	public createMainWindow(options: CreateMainWindowOptions) {
		if (this.windows.has(this.mainWindowName)) {
			throw new Error('Main window has already been created');
		}

		const { url, browserWindowOptions, onReadyToShow } = options;
		const mainWindow = this.createWindow(this.mainWindowName, { url, browserWindowOptions, onReadyToShow });

		return mainWindow;
	}

	public createWindow(name: string, options: CreateWindowOptions) {
		const { url, browserWindowOptions, onReadyToShow } = options;

		if (this.windows.has(name)) {
			this.destroyWindow(name);
		}

		const window = new BrowserWindow(browserWindowOptions);

		window.once('closed', () => this.destroyWindow(name));

		if (import.meta.env.DEV) {
			window.webContents.on('before-input-event', (_, input) => {
				if (input.type === 'keyUp' && input.key === 'F12') {
					window.webContents.openDevTools({ mode: 'detach' });
				}
			});
		}

		this.windows.set(name, window);

		window.loadURL(url).then(onReadyToShow);

		this.events.emit('windowCreated', window);

		return window;
	}

	public getWindow(name: string) {
		return this.windows.get(name);
	}

	public resolveRendererHTML(indexPath: string) {
		if (import.meta.env.DEV) {
			return `http://localhost:${DEV_PORT}/${indexPath}`;
		}

		return this.getHTMLPath(indexPath);
	}

	public getHTMLPath(htmlPath: string) {
		return join(ROOT_PATH, htmlPath);
	}

	public getMainWindow() {
		return this.getWindow(this.mainWindowName);
	}

	public getActiveWindow(): BrowserWindow {
		return BrowserWindow.getFocusedWindow() ?? BrowserWindow.getAllWindows()[0];
	}

	public minimizeWindow(windowName: string) {
		this.windows.get(windowName)?.minimize();
	}

	public closeAllWindows(force = false) {
		for (const name in this.windows) {
			const window = this.windows.get(name)!;
			if (force) {
				window.closable = true;
			}

			window.close();
		}
	}

	public showAboutWindow(options: AboutPanelOptionsOptions = {}) {
		const aboutOptions: AboutPanelOptionsOptions = {
			iconPath: options.iconPath ?? '',
			applicationName: options.applicationName ?? app.getName(),
			applicationVersion: options.applicationVersion ?? app.getVersion(),
			copyright: options.copyright ?? '',
			website: options.website ?? '',
		};

		app.setAboutPanelOptions(aboutOptions);
		app.showAboutPanel();
	}

	public emitMain(channel: IpcChannel, ...args: unknown[]) {
		this.emit(this.mainWindowName, channel, ...args);
	}

	public emit(windowName: string, channel: IpcChannel, ...args: unknown[]) {
		const window = this.getWindow(windowName);

		window?.webContents.send(channel, ...args);
	}

	public emitAll(channel: IpcChannel, ...args: unknown[]) {
		for (const window of this.windows.values()) {
			window?.webContents.send(channel, ...args);
		}
	}

	private destroyWindow(name: string) {
			const window = this.windows.get(name);
			if (!window) {
				return;
			}

			this.events.emit('windowDestroyed', window);
			window.destroy();
			this.windows.delete(name);
	}
}
