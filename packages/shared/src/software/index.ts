import type { Result } from 'neverthrow';

export enum DownloadUrlResolveError {
	Generic,
	HTTPResponseError,
	GitHubRequestError,
	GitHubAssetNotFoundError,
}

export enum SoftwareCategory {
	Audio = 'Audio & Sound',
	Browser = 'Web Browsers',
	Creative = 'Creative',
	Development = 'Development',
	Emulation = 'Emulation',
	FileManagement = 'File Management',
	GameDevelopment = 'Video Game Development',
	Gaming = 'Gaming',
	Media = 'Media',
	Modelling = '3D Modelling',
	Network = 'Network Tools',
	Peripheral = 'Peripherals',
	Productivity = 'Notes & Productivity',
	Runtime = 'Runtimes',
	Security = 'Security',
	Social = 'Social',
	SystemManagement = 'System Management',
	Utility = 'Utilities',
}

export enum PostOperationAction {
	DoNothing,
	Quit,
	LogOut,
	LockSystem,
	RestartSystem,
	ShutDownSystem,
}

export type DownloadOptions = {
	skipInstallation: boolean;
	installSilently: boolean;
	cleanupAfterInstall: boolean;
	openDownloadDir: boolean;
	postOperationAction: PostOperationAction;
};

export interface ISoftwareDefinition {
	key: string;
	name: string;
	category: SoftwareCategory[];
	downloadName: string;
	isArchive?: boolean;
	shouldCacheUrl?: boolean;
	requiresAdmin?: boolean;
	deprecated?: boolean;
	alternative?: ISoftwareDefinition;
	variants?: ISoftwareDefinition[];
	parent?: string;
	icon: string;
	homepage: string;
	resolveDownloadUrl(variantKey?: string): Promise<Result<string, DownloadUrlResolveError>>;
}
