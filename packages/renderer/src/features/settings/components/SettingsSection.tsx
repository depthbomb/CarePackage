import { useId } from 'react';
import type { FC, PropsWithChildren } from 'react';

type SettingsSectionProps = PropsWithChildren & {
	title: string;
	divider?: boolean;
};

export const SettingsSection: FC<SettingsSectionProps> = ({ title, divider = false, children }) => {
	return (
		<>
			<div id={useId()} className="w-full">
				<h3 className="mb-4 text-lg font-display font-bold">{title}</h3>
				<div className="space-y-4">
					{children}
				</div>
			</div>
			{divider && <div className="my-6 w-full h-[1px] bg-gray-700"/>}
		</>
	);
};
