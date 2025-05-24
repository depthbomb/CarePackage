import Icon from '@mdi/react';
import { useState } from 'react';
import { mdiKeyboard } from '@mdi/js';
import { Modal } from '~/components/Modal';
import { TitlebarButton } from './Titlebar/TitlebarButton';
import type { FC } from 'react';
import { KeyCombo } from './KeyCombo';

export const KeyboardShortcutsModal: FC = () => {
	const [show, setShow] = useState(false);

	return (
		<Modal
			shown={show}
			onVisibilityChange={setShow}
			title={
				<div className="space-x-1 flex items-center text-gray-400">
					<Icon path={mdiKeyboard} className="size-5"/>
					<h1 className="font-display font-bold text-xl">Keyboard Shortcuts</h1>
				</div>
			}
			trigger={
				<TitlebarButton action="custom" inner={
					<Icon path={mdiKeyboard} className="size-4"/>
				}/>
			}>
			<div className="space-y-4">
				<div className="space-x-3 flex items-center">
					<KeyCombo keys={['CTRL', 'A']}/> <p>Select all displayed software</p>
				</div>
				<div className="space-x-3 flex items-center">
					<KeyCombo keys={['CTRL', 'D']}/> <p>Deselect all selected software</p>
				</div>
				<div className="space-x-3 flex items-center">
					<KeyCombo keys={['Enter']}/> <p>Continue to the next step</p>
				</div>
				<div className="space-x-3 flex items-center">
					<KeyCombo keys={['Escape']}/> <p>Cancel options select or download &amp; installation step</p>
				</div>
			</div>
		</Modal>
	)
};
