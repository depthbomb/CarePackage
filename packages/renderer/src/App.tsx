import cx from 'clsx';
import Icon from '@mdi/react';
import { useAtom } from 'jotai';
import { useIpc } from './hooks';
import { app } from './atoms/app';
import { IpcChannel } from 'shared';
import { useState, useEffect } from 'react';
import { Button } from './components/Button';
import { Spinner } from './components/Spinner';
import { Titlebar } from './components/Titlebar';
import { DownloadQueue } from './components/DownloadQueue';
import { DownloadOptions } from './components/DownloadOptions';
import { SoftwareCatalogue } from './components/SoftwareCatalogue';
import { useAccentColor } from './hooks/useAccentColor';
import { mdiUpdate, mdiCancel, mdiRefresh, mdiSecurity, mdiArrowLeft, mdiArrowRight, mdiResizeBottomRight } from '@mdi/js';

import logo from '~/assets/img/logo.png';

// TODO This is extremely messy and is due for a cleanup/restructuring.

export const App = () => {
	const [step, setStep]                               = useState(1);
	const [loading, setLoading]                         = useState(true);
	const [windowFocused, setWindowFocused]             = useState(true);
	const [windowMaximized, setWindowMaximized]         = useState(false);
	const [isElevated, setIsElevated]                   = useAtom(app.isElevatedAtom);
	const [isWorking, setIsWorking]                     = useAtom(app.isWorkingAtom);
	const [hasErrors, setHasErrors]                     = useAtom(app.hasErrorsAtom);
	const [updateAvailable, setUpdateAvailable]         = useAtom(app.updateAvailable);
	const [softwareDefinitions, setSoftwareDefinitions] = useAtom(app.softwareDefinitionsAtom);
	const [softwareVariants, setSoftwareVariants]       = useAtom(app.softwareVariantsAtom);
	const [selectedSoftware, setSelectedSoftware]       = useAtom(app.selectedSoftwareAtom);
	const [skipInstallation]                            = useAtom(app.skipInstallationAtom);
	const [installSilently]                             = useAtom(app.installSilentlyAtom);
	const [cleanupAfterInstall]                         = useAtom(app.cleanupAfterInstallAtom);
	const [openDownloadDir, setOpenDownloadDir]         = useAtom(app.openDownloadDirAtom);
	const [postOperationAction]                         = useAtom(app.postOperationActionAtom);
	const [onFocused]                                   = useIpc(IpcChannel.MainWindow_Focused);
	const [onBlurred]                                   = useIpc(IpcChannel.MainWindow_Blurred);
	const [onMaximized]                                 = useIpc(IpcChannel.MainWindow_Maximized);
	const [onUnmaximized]                               = useIpc(IpcChannel.MainWindow_Restored);
	const [onOutdated]                                  = useIpc(IpcChannel.Updater_Outdated);

	useAccentColor();

	const performPrimaryAction = async () => {
		// Step 1 = Catalogue
		// Step 2 = Options
		// Step 3 = Download Queue

		if (selectedSoftware.length === 0) {
			return;
		}

		if (step === 2) {
			if (selectedSoftware.filter(sw => sw.requiresAdmin).length > 0 && !skipInstallation && !isElevated) {
				const { response } = await window.api.showMessageBox({
					type: 'info',
					title: 'Elevated privileges required',
					message: 'One or more of the selected software requires elevated privileges to install. Would you like to restart CarePackage as administrator?\nIf you choose not to, then the folder containing the downloaded software will be opened after everything else has finished installing.',
					buttons: ['Yes', 'No', 'Cancel'],
					defaultId: 0,
				});
				if (response === 0) {
					window.api.restartAsElevated(selectedSoftware.map(s => s.key));
					return;
				} else if (response === 1) {
					setOpenDownloadDir(true);
				} else {
					return;
				}
			}

			if (selectedSoftware.filter(sw => sw.isArchive).length > 0 && !openDownloadDir) {
				const { response } = await window.api.showMessageBox({
					type: 'warning',
					title: 'Downloading archive files',
					message: 'One or more of the selected software will be downloaded as compressed archives. Would you like to open the folder containing the downloaded files when everything is done downloading?',
					buttons: ['Yes', 'No', 'Cancel'],
					defaultId: 0,
				});
				if (response === 0) {
					setOpenDownloadDir(true);
				} else if (response === 2) {
					return;
				}
			}

			window.api.startDownload(selectedSoftware.map(sw => sw.key), {
				skipInstallation,
				installSilently,
				cleanupAfterInstall,
				openDownloadDir,
				postOperationAction,
			});

			setIsWorking(true);
		}

		setStep(p => p + 1);
	};

	const performSecondaryAction = async () => {
		// Step 1 = Catalogue
		// Step 2 = Options
		// Step 3 = Download Queue

		switch (step) {
			case 1:
				setSelectedSoftware([]);
				break;
			case 2:
				setStep(1);
				break;
			case 3:
				setHasErrors(false);
				setSelectedSoftware([]);
				setStep(1);
				await window.api.cancelDownload();
				break;
		}

		setIsWorking(false);
	};

	const onUpdateButtonClick = async () => {
		await window.api.openExternalUrl('https://github.com/depthbomb/CarePackage/releases/latest');
	};

	useEffect(() => {
		window.api.isElevated().then(setIsElevated);
		window.api.getSoftwareDefinitions()
			.then(({ definitions, variants }) => {
				setSoftwareDefinitions(definitions);
				setSoftwareVariants(variants);
				setLoading(false);
			});
	}, []);

	useEffect(() => {
		if (!isWorking && !hasErrors) {
			setStep(1);
		}
	}, [isWorking, hasErrors]);

	useEffect(() => {
		if (!loading) {
			const params = new URLSearchParams(window.location.search);
			if (params.get('software')) {
				const keys = params.get('software')!.split(',');
				setSelectedSoftware(softwareDefinitions.filter(s => keys.includes(s.key)));
			}
		}
	}, [loading]);

	useEffect(() => {
		onFocused(() => setWindowFocused(true));
		onBlurred(() => setWindowFocused(false));
		onOutdated(() => setUpdateAvailable(true));
		onMaximized(() => setWindowMaximized(true));
		onUnmaximized(() => setWindowMaximized(false));
	}, []);

	return (
		<div className={cx('relative w-full h-screen flex flex-col items-stretch border', windowMaximized ? 'border-gray-900' : windowFocused ? 'border-accent-500' : 'border-gray-700')}>
			<Titlebar/>
			<header className="px-5 h-15 flex items-center shrink-0">
				<img src={logo} className="mr-2 size-8" width="32" height="32" draggable="false"/>
				<div className="flex items-center">
					<span className="h-auto text-2xl font-display font-bold">CarePackage</span>
					{isElevated && (
						<div className="ml-2 py-0.5 px-1.5 flex items-center font-mono text-xs uppercase text-yellow-500 bg-yellow-950 border border-yellow-500 rounded-full">
							<Icon path={mdiSecurity} className="mr-1 size-3"/>
							<span>Administrator</span>
						</div>
					)}
				</div>
			</header>
			{loading ? (
				<div className="space-y-4 size-full flex flex-col items-center justify-center">
					<Spinner className="size-18"/>
					<p className="font-semibold">Loading software definitions&hellip;</p>
				</div>
			) : (
				<main className="px-5 h-[calc(100%-60px-62px)]">
					{step === 1 && <SoftwareCatalogue software={softwareDefinitions}/>}
					{step === 2 && <DownloadOptions/>}
					{step === 3 && <DownloadQueue/>}
				</main>
			)}
			{!loading && (
				<footer className="py-4 px-5 space-x-2 flex items-center">
					{hasErrors ? (
						<Button onClick={() => {
							setHasErrors(false);
							setSelectedSoftware([]);
							setStep(1);
						}}>
							<Icon path={mdiArrowLeft} className="size-4"/>
							<span>Return to catalogue</span>
						</Button>
					) : (
						<>
							<Button
								variant="accent"
								onClick={performPrimaryAction}
								disabled={selectedSoftware.length === 0 || step === 3}>
								<span>Continue</span>
								<Icon path={mdiArrowRight} className="size-4"/>
							</Button>
							{step === 1 && (
								<Button onClick={performSecondaryAction} disabled={selectedSoftware.length === 0}>
									<Icon path={mdiRefresh} className="size-4"/>
									<span>Reset</span>
								</Button>
							)}
							{(step === 2 || step === 3) && (
								<Button onClick={performSecondaryAction} disabled={selectedSoftware.length === 0} variant="danger">
									<Icon path={mdiCancel} className="size-4"/>
									<span>Cancel</span>
								</Button>
							)}
						</>
					)}
					{import.meta.env.DEV && (
						<Button onClick={() => {
							const softwareWithoutVariants = softwareDefinitions.filter(sw => sw.variants!.length === 0);
							setSelectedSoftware([...softwareWithoutVariants, ...softwareVariants]);
						}} disabled={isWorking}>
							<span>Select all</span>
						</Button>
					)}
					{import.meta.env.DEV && <p className="shrink-0">DEBUG: Step #{step}</p>}
					{updateAvailable && (
						<Button onClick={onUpdateButtonClick} variant="brand" size="sm" className="ml-auto">
							<Icon path={mdiUpdate} className="size-3"/>
							<span>Update available!</span>
						</Button>
					)}
				</footer>
			)}
			{!windowMaximized && (
				<div className="absolute right-0 bottom-0">
					<Icon path={mdiResizeBottomRight} className="size-6 text-gray-600"/>
				</div>
			)}
		</div>
	);
};
