import Icon from '@mdi/react';
import { useAtom } from 'jotai';
import { app } from '~/atoms/app';
import { useSetting } from '~/hooks';
import { mdiTrashCan } from '@mdi/js';
import { Alert } from '~/components/Alert';
import { Modal } from '~/components/Modal';
import { Input } from '~/components/Input';
import { mdiCog, mdiAlert } from '@mdi/js';
import { useState, useEffect } from 'react';
import { Button } from '~/components/Button';
import { Switch } from '~/components/Switch';
import { ByteSize, SettingsKey } from 'shared';
import { Fieldset } from '~/components/Fieldset';
import { SettingsSection } from './components/SettingsSection';
import { TitlebarButton } from '~/components/Titlebar/TitlebarButton';
import type { FC, ChangeEvent } from 'react';

export const SettingsModal: FC = () => {
	const [show, setShow]                                     = useState(false);
	const [totalFiles, setTotalFiles]                         = useState(0);
	const [totalSize, setTotalSize]                           = useState(0);
	const [sweepButtonDisabled, setSweepButtonDisabled]       = useState(true);
	const [isWorking]                                         = useAtom(app.isWorkingAtom);
	const [showCategoryBadges, setShowCategoryBadges]         = useSetting<boolean>(SettingsKey.UI_ShowCategoryBadges, { reactive: false });
	const [maxTries, setMaxTries]                             = useSetting<number>(SettingsKey.Aria2_MaxTries, { reactive: false });
	const [maxConcurrentDownloads, setMaxConcurrentDownloads] = useSetting<number>(SettingsKey.Aria2_MaxConcurrentDownloads, { reactive: false });
	const [maxDownloadLimit, setMaxDownloadLimit]             = useSetting<string>(SettingsKey.Aria2_MaxDownloadLimit);

	useEffect(() => {
		if (!show) {
			return;
		}

		window.api.calculateDownloadsSize().then(([totalFiles, totalSize]) =>{
			setTotalFiles(totalFiles);
			setTotalSize(totalSize);
		});
	}, [show]);

	useEffect(() => setSweepButtonDisabled(totalFiles === 0 && totalSize === 0), [totalFiles, totalSize]);

	const onMaxTriesInputChanged = (e: ChangeEvent<HTMLInputElement>) => setMaxTries(parseInt(e.target.value));
	const onMaxConcurrentDownloadsInputChanged = (e: ChangeEvent<HTMLInputElement>) => setMaxConcurrentDownloads(parseInt(e.target.value));
	const onMaxDownloadLimitInputChanged = (e: ChangeEvent<HTMLInputElement>) => {
		const { value } = e.target;
		setMaxDownloadLimit(value);
	};
	const onSweepButtonClicked = async () => {
		setSweepButtonDisabled(true);

		await window.api.performSweep();

		setTotalFiles(0);
		setTotalSize(0);
	};

	return (
		<Modal
			shown={show}
			onVisibilityChange={setShow}
			title={
				<div className="space-x-1 flex items-center text-gray-400">
					<Icon path={mdiCog} className="size-5"/>
					<h1 className="font-display font-bold text-xl">Settings</h1>
				</div>
			}
			trigger={
				<TitlebarButton disabled={isWorking} action="custom" inner={
					<Icon path={mdiCog} className="size-4"/>
				}/>
			}>
			<div className="flex flex-col">
				<SettingsSection title="Interface" divider>
					<Fieldset>
						<Switch
							label="Show software categories"
							checked={showCategoryBadges}
							onCheckedChange={setShowCategoryBadges}/>
					</Fieldset>
				</SettingsSection>
				<SettingsSection title="Downloads" divider>
					<Alert icon={mdiAlert} variant="warning">
						<p>Changes to these settings requires an app restart.</p>
					</Alert>
					<Fieldset>
						<label>Max tries</label>
						<Input onChange={onMaxTriesInputChanged} value={maxTries} min={0} type="number" className="w-full"/>
						<p className="text-xs">Use <code>0</code> for unlimited.</p>
					</Fieldset>
					<Fieldset>
						<label>Max concurrent downloads</label>
						<Input onChange={onMaxConcurrentDownloadsInputChanged} value={maxConcurrentDownloads} min={1} max={10} type="number" className="w-full"/>
						<p className="text-xs">Increasing this setting can result in using drastically more bandwidth when downloading.</p>
					</Fieldset>
					<Fieldset>
						<label>Max overall download speed</label>
						<Input onChange={onMaxDownloadLimitInputChanged} value={maxDownloadLimit} type="text" className="w-full"/>
						<p className="text-xs">Use <code>0</code> for unlimited. Examples: <code>100K</code>, <code>20M</code>, <code>1G</code>.</p>
					</Fieldset>
				</SettingsSection>
				<SettingsSection title="Cleanup">
					<Button variant="danger" onClick={onSweepButtonClicked} size="sm" disabled={sweepButtonDisabled}>
						<Icon path={mdiTrashCan} className="size-4"/>
						<span>Clean up downloads</span>
					</Button>
					{(totalFiles > 0 && totalSize > 0) && (
						<p className="text-sm">There are {totalFiles} file(s) totalling {ByteSize.formatSize(totalSize)} to delete.</p>
					)}
				</SettingsSection>
			</div>
		</Modal>
	)
};
