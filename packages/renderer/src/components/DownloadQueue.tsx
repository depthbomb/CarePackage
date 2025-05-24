import { useAtom } from 'jotai';
import { useIpc } from '~/hooks';
import { app } from '~/atoms/app';
import { Spinner } from './Spinner';
import { IpcChannel } from 'shared';
import { useState, useEffect } from 'react';
import type { FC } from 'react';
import type { ISoftwareDefinition } from 'shared';

type ErroredSoftware = {
	software: ISoftwareDefinition;
	error: string;
};

type QueuedSoftware = ISoftwareDefinition & {
	progress: number;
	status: string;
	spinner?: boolean;
};

export const DownloadQueue: FC = () => {
	const [,setIsWorking]                         = useAtom(app.isWorkingAtom);
	const [selectedSoftware, setSelectedSoftware] = useAtom(app.selectedSoftwareAtom);
	const [skipInstallation]                      = useAtom(app.skipInstallationAtom);
	const [softwareQueue, setSoftwareQueue]       = useState<QueuedSoftware[]>(selectedSoftware.map(sw => ({ ...sw, progress: 0, status: 'In queue' })));
	const [erroredSoftware, setErroredSoftware]   = useState<ErroredSoftware[]>([]);
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
		onResolvingDownloadUrl((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: 'Resolving download URL...', spinner: true }));
		});
		onUrlResolveError((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: 'Error resolving download URL', spinner: false }));
		});
		onResolvedDownloadUrl((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: 'Waiting to download...', spinner: false }));
		});
		onDownloadStarted((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: 'Downloading...', spinner: true }));
		});
		onDownloadError((software: ISoftwareDefinition, error: string) => {
			setSoftwareQueue(p => p.filter(s => s.key !== software.key));
			setErroredSoftware(p => [...p, { software, error }]);
		});
		onDownloadCompleted((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(
				software.key,
				() => ({
					status: (skipInstallation || software.isArchive) ? 'Done' : 'Waiting for downloads to finish...',
					spinner: false
				})
			);
		});
		onDownloadsFinished(() => {
			if (skipInstallation) {
				return;
			}

			for (const sw of softwareQueue.filter(sw => !sw.isArchive)) {
				updateSoftwareInQueue(sw.key, () => ({ status: 'Waiting to install...', spinner: false }));
			}
		});
		onRunningExecutable((software: ISoftwareDefinition) => {
			updateSoftwareInQueue(software.key, () => ({ status: `Waiting for ${software.downloadName} to exit...`, spinner: true }));
		});
		onExecutableExited((software: ISoftwareDefinition) => {
			setSoftwareQueue(p => p.filter(s => s.key !== software.key));
		});
		onAllDone(() => {
			setIsWorking(false);
			setSelectedSoftware([]);
			setSoftwareQueue([]);
		});
	}, []);


	return (
		<div className="space-y-5 h-full flex flex-col items-center">
			<div className="size-full flex flex-col bg-gray-950 rounded-xs border border-gray-700 overflow-y-auto [scrollbar-width:thin]">
				{softwareQueue.map((sw, i) => (
					<div key={sw.key} className="p-3 space-x-2 flex items-center">
						<p className="font-bold font-mono text-gray-400">{i + 1}.</p>
						<img src={`software-icon://${sw.icon}`} className="size-8" width="32" height="32" draggable="false"/>
						<p className="mr-auto font-display">{sw.name}</p>
						{sw.spinner && <Spinner className="size-5"/>}
						<p className="text-sm font-mono">{sw.status}</p>
					</div>
				))}
				{erroredSoftware.map(({ software, error }) => (
					<div key={software.key} className="p-3 space-x-2 flex items-center bg-red-900">
						<img src={`software-icon://${software.icon}`} className="size-6" width="24" height="24" draggable="false"/>
						<p>{software.name} &mdash; <span className="font-bold">{error}</span></p>
					</div>
				))}
			</div>
		</div>
	);
};
