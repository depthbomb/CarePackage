import type { IpcChannel } from './ipc';
import type { SettingsKey } from './settings';
import type { DownloadOptions, ISoftwareDefinition } from './software';
import type { MessageBoxOptions, MessageBoxReturnValue } from 'electron';

export type Awaitable<T> = PromiseLike<T> | T;
export type Maybe<T>     = T | undefined;
export type Nullable<T>  = T | null;

export type VersionsApi = typeof process.versions;

export type IpcApi = {
	on: (channel: IpcChannel, listener: (...args: any[]) => void) => () => void;
	once: (channel: IpcChannel, listener: (...args: any[]) => void) => void;
	off: (channel: IpcChannel, listener: (...args: any[]) => void) => void;
	removeAllListeners: (channel: IpcChannel) => void;
};

export type CoreApi = {
	showMessageBox(options: MessageBoxOptions): Promise<MessageBoxReturnValue>;
	isElevated(): Promise<boolean>;
	restartAsElevated(softwareKeys: string[]): Promise<void>;
	openExternalUrl(url: string): Promise<void>;
	//
	minimizeWindow(): Promise<void>;
	maximizeWindow(): Promise<void>;
	restoreWindow(): Promise<void>;
	closeWindow(): Promise<void>;
	//
	getSettingsValue<T>(key: SettingsKey, defaultValue?: any, secure?: boolean): Promise<T>;
	setSettingsValue(key: SettingsKey, value: any, secure?: boolean): Promise<void>;
	resetSettings(): Promise<void>;
	//
	getSoftwareDefinitions(): Promise<ISoftwareDefinition[]>;
	startDownload(keys: string[], options: DownloadOptions): Promise<void>;
	cancelDownload(): Promise<void>;
	showSoftwareMenu(key: string): Promise<void>;
	//
	calculateDownloadsSize(): Promise<[number, number]>;
	performSweep(): Promise<void>;
};

export type SystemApi = {
	arch: () => string;
	type: () => string;
	release: () => string;
	platform: () => NodeJS.Platform;
	hostname: () => string;
};

export type SettingsApi = {
	getValue: <T>(key: SettingsKey, defaultValue?: unknown, secure?: boolean) => T
};
