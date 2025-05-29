import cx from 'clsx';
import Icon from '@mdi/react';
import { useAtom } from 'jotai';
import { useIpc } from '~/hooks';
import { app } from '~/atoms/app';
import { Spinner } from './Spinner';
import { IpcChannel } from 'shared';
import { useState, useEffect } from 'react';
import { mdiClose, mdiCheck, mdiDownload, mdiTimerSand, mdiLinkVariant } from '@mdi/js';
import type { FC } from 'react';
import type { ISoftwareDefinition } from 'shared';

type QueuedSoftware = ISoftwareDefinition & {
	status: Statuses;
	spinner?: boolean;
	error?: boolean;
};

type StatusIconProps = {
	status: Statuses;
};

const enum Statuses {
	WaitingForAria2 = 'Waiting for download manager',
	InQueue = 'In queue',
	ResolvingDownloadUrl = 'Resolving download URL',
	ErrorResolvingDownloadUrl = 'Error resolving download URL',
	WaitingToDownload = 'Waiting to download',
	Downloading = 'Downloading',
	DownloadFailed = 'Download failed',
	Done = 'Done',
	WaitingForDownloads = 'Waiting for downloads to finish',
	WaitingToInstall = 'Waiting to install',
	WaitingForExecutable = 'Waiting for installer to finish'
}

const getStatusIconPath = (status: Statuses) => {
	switch (status) {
		case Statuses.WaitingForAria2:
		case Statuses.WaitingForDownloads:
		case Statuses.WaitingToInstall:
		case Statuses.WaitingForExecutable:
		case Statuses.WaitingToDownload:
		case Statuses.InQueue:
			return mdiTimerSand;
		case Statuses.ResolvingDownloadUrl:
			return mdiLinkVariant;
		case Statuses.DownloadFailed:
		case Statuses.ErrorResolvingDownloadUrl:
			return mdiClose;
		case Statuses.Downloading:
			return mdiDownload;
		case Statuses.Done:
			return mdiCheck;
	}
};

const StatusIcon: FC<StatusIconProps> = ({ status }) => {
	return (
		<span className="flex items-center justify-center">
			<Icon path={getStatusIconPath(status)} className="size-6"/>
		</span>
	);
};

export const DownloadQueue: FC = () => {
	const [,setIsWorking]                         = useAtom(app.isWorkingAtom);
	const [,setHasErrors]                         = useAtom(app.hasErrorsAtom);
	const [selectedSoftware, setSelectedSoftware] = useAtom(app.selectedSoftwareAtom);
	const [skipInstallation]                      = useAtom(app.skipInstallationAtom);
	const [softwareQueue, setSoftwareQueue]       = useState<QueuedSoftware[]>(selectedSoftware.map(sw => ({ ...sw, status: Statuses.WaitingForAria2 })));
	const [onAria2Ready]                          = useIpc(IpcChannel.Aria2_Ready);
	const [onResolvingDownloadUrl]                = useIpc(IpcChannel.Software_ResolvingDownloadUrl);
	const [onUrlResolveError]                     = useIpc(IpcChannel.Software_UrlResolveError);
	const [onResolvedDownloadUrl]                 = useIpc(IpcChannel.Software_ResolvedDownloadUrl);
	const [onDownloadStarted]                     = useIpc(IpcChannel.Software_DownloadStarted);
	const [onDownloadError]                       = useIpc(IpcChannel.Software_DownloadError);
	const [onDownloadCompleted]                   = useIpc(IpcChannel.Software_DownloadCompleted);
	const [onDownloadsFinished]                   = useIpc(IpcChannel.Software_DownloadsFinished);
	const [onRunningExecutable]                   = useIpc(IpcChannel.Software_RunningExecutable);
	const [onExecutableExited]                    = useIpc(IpcChannel.Software_ExecutableExited);
	const [onAllDone]                             = useIpc(IpcChannel.Software_AllDone);

	const updateSoftwareInQueue = (key: string, update: (sw: QueuedSoftware) => Partial<QueuedSoftware>) => {
		setSoftwareQueue(queue =>
			queue.map(item =>
				item.key === key ? { ...item, ...update(item) } : item
			)
		);
	};

	useEffect(() => {
		onAria2Ready(() => {
			setSoftwareQueue(queue => queue.map(item => {
				item.status = Statuses.InQueue;
				return { ...item };
			}));
		});
		onResolvingDownloadUrl((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: Statuses.ResolvingDownloadUrl, spinner: true }));
		});
		onUrlResolveError((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ error: true, status: Statuses.ErrorResolvingDownloadUrl, spinner: false }));
		});
		onResolvedDownloadUrl((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: Statuses.WaitingToDownload, spinner: false }));
		});
		onDownloadStarted((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: Statuses.Downloading, spinner: true }));
		});
		onDownloadError((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ error: true, status: Statuses.DownloadFailed, spinner: false }));
		});
		onDownloadCompleted((software: ISoftwareDefinition) => {
			if (skipInstallation) {
				setSoftwareQueue(p => p.filter(s => s.key !== software.key));
			} else {
				updateSoftwareInQueue(
					software.key,
					() => ({
						status: software.isArchive ? Statuses.Done : Statuses.WaitingForDownloads,
						spinner: false
					})
				);
			}
		});
		onDownloadsFinished(async () => {
			if (skipInstallation) {
				return;
			}

			setSoftwareQueue(queue =>
				queue.map(item => {
					item.status = Statuses.WaitingToInstall;
					item.spinner = false;
					return { ...item };
				})
			);
		});
		onRunningExecutable((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: Statuses.WaitingForExecutable, spinner: true }));
		});
		onExecutableExited((software: ISoftwareDefinition) => {
			setSoftwareQueue(p => p.filter(s => s.key !== software.key));
		});
		onAllDone((hasErrors: boolean) => {
			setHasErrors(hasErrors);
			setIsWorking(false);
			if (!hasErrors) {
				setSoftwareQueue([]);
			}

			setSelectedSoftware([]);
		});
	}, []);


	return (
		<div className="space-y-5 h-full flex flex-col items-center">
			<div className="size-full flex flex-col bg-gray-950 rounded-xs border border-gray-700 overflow-y-auto [scrollbar-width:thin]">
				{softwareQueue.map(sw => (
					<div key={sw.key} className={cx('p-3 space-x-2 flex items-center', sw.error && 'bg-red-900')}>
						<StatusIcon status={sw.status}/>
						<img src={`software-icon://${sw.icon}`} className="size-8" width="32" height="32" draggable="false"/>
						<p className="mr-auto font-display">{sw.name}</p>
						{sw.spinner && <Spinner className="size-5"/>}
						<p className="text-sm font-mono">{sw.status}</p>
					</div>
				))}
			</div>
		</div>
	);
};
