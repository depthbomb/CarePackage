import { Input } from './Input';
import { useAtom } from 'jotai';
import { app } from '~/atoms/app';
import { useSetting } from '~/hooks';
import { Select } from './Input/Select';
import { SoftwareRow } from './SoftwareRow';
import { useState, useEffect } from 'react';
import { SettingsKey, SoftwareCategory } from 'shared';
import type { FC, ChangeEvent } from 'react';
import type { Maybe, ISoftwareDefinition } from 'shared';

type SoftwareCatalogueProps = {
	software: ISoftwareDefinition[];
};

export const SoftwareCatalogue: FC<SoftwareCatalogueProps> = ({ software }) => {
	const [searchedName, setSearchedName]         = useState('');
	const [category, setCategory]                 = useState<Maybe<SoftwareCategory>>();
	const [filteredSoftware, setFilteredSoftware] = useState<ISoftwareDefinition[]>(software);
	const [selectedSoftware]                      = useAtom(app.selectedSoftwareAtom);
	const [showCategoryBadges]                    = useSetting<boolean>(SettingsKey.UI_ShowCategoryBadges, { reactive: true });

	const onSearchChange = (event: ChangeEvent<HTMLInputElement>) => {
		setSearchedName(event.target.value);
	};

	const onCategoryChange = (event: ChangeEvent<HTMLSelectElement>) => {
		setCategory(event.target.value as SoftwareCategory);
	};

	useEffect(() => {
		if (searchedName !== '') {
			setFilteredSoftware(
				software.filter(sw => sw.name.toLowerCase().includes(searchedName))
			);
		} else {
			setFilteredSoftware(
				category ? software.filter(sw => sw.category.includes(category)) : software
			);
		}
	}, [software, searchedName, category, setFilteredSoftware]);

	return (
		<div className="space-y-3 h-full flex flex-col">
			<div className="space-x-2.5 flex items-end">
				<Input onChange={onSearchChange} placeholder="Search software"/>
				<Select disabled={searchedName !== ''} onChange={onCategoryChange}>
					<option value="">All categories</option>
					{Object.values(SoftwareCategory).sort().map((cat) => (
						<option key={cat} value={cat}>{cat}</option>
					))}
				</Select>
				{selectedSoftware.length > 0 && <p className="ml-auto">{selectedSoftware.length} selected</p>}
			</div>
			{filteredSoftware.length ? (
				<div className="h-full bg-gray-950 rounded-xs border border-gray-700 overflow-auto [scrollbar-width:thin]">
					{filteredSoftware.map(sw => <SoftwareRow key={sw.key} software={sw} showCategoryBadges={showCategoryBadges}/>)}
				</div>
			) : (
				<div className="size-full flex flex-col items-center justify-center">
					<p className="text-8xl text-gray-800">¯\_(ツ)_/¯</p>
				</div>
			)}
		</div>
	);
};
