import { useAtom } from 'jotai';
import { app } from '~/atoms/app';
import { Switch } from './Switch';
import { Select } from './Input/Select';
import { useState, useEffect } from 'react';
import { PostOperationAction } from 'shared';
import type { FC, ChangeEvent } from 'react';

export const DownloadOptions: FC = () => {
	const [helpIndex, setHelpIndex]                     = useState(-1);
	const [skipInstallation, setSkipInstallation]       = useAtom(app.skipInstallationAtom);
	const [installSilently, setInstallSilently]         = useAtom(app.installSilentlyAtom);
	const [cleanupAfterInstall, setCleanupAfterInstall] = useAtom(app.cleanupAfterInstallAtom);
	const [openDownloadDir, setOpenDownloadDir]         = useAtom(app.openDownloadDirAtom);
	const [,setPostOperationAction]                     = useAtom(app.postOperationActionAtom);

	const onPostOperationActionSelectChange = (e: ChangeEvent<HTMLSelectElement>) => setPostOperationAction(parseInt(e.target.value));

	useEffect(() => {
		if (skipInstallation) {
			setInstallSilently(false);
			setCleanupAfterInstall(false);
		}

		if (installSilently) {
			setSkipInstallation(false);
		}
	}, [skipInstallation, installSilently, setSkipInstallation, setInstallSilently, setCleanupAfterInstall]);

	return (
		<div className="h-full grid grid-cols-2">
			<div className="space-y-5 h-full flex flex-col">
				<Switch
					label="Skip installation"
					checked={skipInstallation}
					onCheckedChange={setSkipInstallation}
					onMouseOver={() => setHelpIndex(1)}
					disabled={installSilently}/>
				<Switch
					label="Try to install silently"
					checked={installSilently}
					onCheckedChange={setInstallSilently}
					onMouseOver={() => setHelpIndex(2)}
					disabled={skipInstallation}/>
				<Switch
					label="Delete executables after installation"
					checked={cleanupAfterInstall}
					onCheckedChange={setCleanupAfterInstall}
					onMouseOver={() => setHelpIndex(3)}
					disabled={skipInstallation}/>
				<Switch
					label="Open download path after installation"
					checked={openDownloadDir}
					onCheckedChange={setOpenDownloadDir}
					onMouseOver={() => setHelpIndex(4)}/>
				<fieldset className="space-x-2.5 flex items-center">
					<label>When done:</label>
					<Select defaultValue={PostOperationAction.DoNothing} onChange={onPostOperationActionSelectChange} onMouseOver={() => setHelpIndex(5)}>
						<option value={PostOperationAction.DoNothing}>Do nothing</option>
						<option value={PostOperationAction.Quit}>Quit</option>
						<option value={PostOperationAction.LogOut}>Log out</option>
						<option value={PostOperationAction.LockSystem}>Lock system</option>
						<option value={PostOperationAction.RestartSystem}>Restart system</option>
						<option value={PostOperationAction.ShutDownSystem}>Shut down system</option>
					</Select>
				</fieldset>
			</div>
			<div className="p-3 space-y-3 h-full bg-gray-950 rounded-xs border border-gray-700">
				{helpIndex < 1 && (
					<p>Hover over and option to read more about it here!</p>
				)}
				{helpIndex === 1 && (
					<>
						<p>When this option is enabled, software will only be downloaded and the installation step will be skipped.</p>
						<p>Enabling this option disabled <strong>Try to install silently</strong> and <strong>Delete executables after installation</strong>.</p>
						<p>You should enable <strong>Open download path after installation</strong> with this option to view the downloaded software.</p>
					</>
				)}
				{helpIndex === 2 && (
					<>
						<p>When this option is enabled, CarePackage will attempt to pass arguments to the installer that will hide the installer window and require no user input.</p>
						<p>This doesn't work for every installer and may actually cause issues with the installation. Disable this option if you start to get failed installations.</p>
					</>
				)}
				{helpIndex === 3 && (
					<p>When this option is enabled, CarePackage will delete the installer of software after it has successfully exited.</p>
				)}
				{helpIndex === 4 && (
					<p>When this option is enabled, CarePackage will open the folder containing the downloaded software when everything is done downloading &amp; installing &mdash; if you chose to install software.</p>
				)}
				{helpIndex === 5 && (
					<>
						<p>This option determines what CarePackage should do after everything is done downloading and installed.</p>
						<p>The <strong>Restart system</strong> and <strong>Shut down system</strong> actions cannot be cancelled unless you run <code className="py-0.25 px-1 bg-gray-700 rounded-sm">shutdown /a</code> in <i>cmd</i> or <i>Terminal</i>.</p>
					</>
				)}
			</div>
		</div>
	);
};
