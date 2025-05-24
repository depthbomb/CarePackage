import { useIpc } from '~/hooks';
import { IpcChannel } from 'shared';
import { useState, useEffect } from 'react';
import { TitlebarButton } from './TitlebarButton';
import { AboutModal } from '~/components/AboutModal';
import { SettingsModal } from '~/features/settings/SettingsModal';
import { KeyboardShortcutsModal } from '~/components/KeyboardShortcutsModal';
import type { FC } from 'react';

export const Titlebar: FC = () => {
	const [isMaximized, setIsMaximized] = useState(false);
	const [onWindowMaximized]           = useIpc(IpcChannel.MainWindow_Maximized);
	const [onWindowRestored]            = useIpc(IpcChannel.MainWindow_Restored);

	useEffect(() => {
		onWindowMaximized(() => setIsMaximized(true));
		onWindowRestored(()  => setIsMaximized(false));
	}, []);

	return (
		<div className="absolute top-0 right-0 w-screen h-15 flex items-stretch z-[9002]">
			<div className="w-full draggable"/>
			<AboutModal/>
			<KeyboardShortcutsModal/>
			<SettingsModal/>
			<TitlebarButton onClick={() => window.api.minimizeWindow()} action="minimize"/>
			<TitlebarButton onClick={() => isMaximized ? window.api.restoreWindow() : window.api.maximizeWindow()} action={isMaximized ? 'restore' : 'maximize'}/>
			<TitlebarButton onClick={() => window.api.closeWindow()} action="close"/>
		</div>
	);
};
