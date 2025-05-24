import Icon from '@mdi/react';
import { useState } from 'react';
import { Anchor } from './Anchor';
import { Modal } from '~/components/Modal';
import { mdiInformationOutline } from '@mdi/js';
import { product, GIT_HASH_SHORT } from 'shared';
import { TitlebarButton } from './Titlebar/TitlebarButton';
import type { FC } from 'react';

export const AboutModal: FC = () => {
	const [show, setShow] = useState(false);

	return (
		<Modal
			shown={show}
			onVisibilityChange={setShow}
			title={
				<div className="space-x-1 flex items-center text-gray-400">
					<h1 className="space-x-2 flex items-center">
						<span className="font-display font-bold text-xl">CarePackage</span>
						<span className="text-sm font-mono">{product.version}+{GIT_HASH_SHORT}</span>
					</h1>
				</div>
			}
			trigger={
				<TitlebarButton action="custom" inner={
					<Icon path={mdiInformationOutline} className="size-4"/>
				}/>
			}>
			<div className="space-y-4 flex flex-col">
				<p>CarePackage is a desktop application for Windows 10/11 heavily inspired by <Anchor href="https://ninite.com" target="_blank">Ninite</Anchor> that makes it quick and easy to download and install all of your favorite programs at once.</p>
				<p>CarePackage's intended use case is to be used on a new installation of Windows, but of course you can use it however you'd like!</p>
				<div className="mt-auto space-x-4">
					<Anchor href="https://github.com/depthbomb/CarePackage" target="_blank">GitHub</Anchor>
					<Anchor href="https://github.com/depthbomb/CarePackage/issues/new/choose" target="_blank">Suggest a program</Anchor>
				</div>
			</div>
		</Modal>
	)
};
