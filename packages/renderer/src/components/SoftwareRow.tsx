import cx from 'clsx';
import Icon from '@mdi/react';
import { useAtom } from 'jotai';
import { app } from '~/atoms/app';
import { mdiAlert } from '@mdi/js';
import { useState, useEffect } from 'react';
import type { FC } from 'react';
import type { ISoftwareDefinition } from 'shared';

import uacIcon from '~/assets/img/uac.png';
import zipIcon from '~/assets/img/zip.png';

type SoftwareRowProps = {
	software: ISoftwareDefinition;
	showCategoryBadges?: boolean;
};

export const SoftwareRow: FC<SoftwareRowProps> = ({ software, showCategoryBadges = true }) => {
	const [selected, setSelected]                 = useState(false);
	const [selectedSoftware, setSelectedSoftware] = useAtom(app.selectedSoftwareAtom);

	const onClicked = () => {
		setSelectedSoftware(p => p.includes(software) ? p.filter(sw => sw !== software) : [...p, software]);
	};

	useEffect(() => setSelected(selectedSoftware.includes(software)), [software, setSelected, selectedSoftware]);

	return (
		<a
			key={software.key}
			className={cx('p-3 space-x-3 w-full flex items-center cursor-pointer', selected ? 'text-white bg-gradient-to-r from bg-rose-500 to-gray-950' : 'text-gray-300 hover:text-white hover:bg-gray-800')}
			onClick={onClicked}
			onContextMenu={() => window.api.showSoftwareMenu(software.key)}
		>
			<img src={`software-icon://${software.icon}`} className="drop-shadow drop-shadow-black/33" alt={software.name} draggable="false"/>
			<p className={cx('font-display text-lg text-shadow-lg', selected && 'font-bold')}>{software.name}</p>
			{software.deprecated && <Icon path={mdiAlert} className="size-5 text-red-600"/>}
			{software.requiresAdmin && <img className="size-4" src={uacIcon} width="16" height="16" draggable="false"/>}
			{software.isArchive && <img className="size-4" src={zipIcon} width="16" height="16" draggable="false"/>}
			{showCategoryBadges && (
				<div className="ml-auto space-x-1 flex items-center">
					{software.category.map((cat) => (
						<span key={cat} className="py-0.5 px-1.5 text-gray-400 font-mono text-xs bg-gray-900 border rounded-full">{cat}</span>
					))}
				</div>
			)}
		</a>
	);
};
