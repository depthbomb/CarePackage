import type { FC } from 'react';

type KeyComboProps = {
	keys: string[];
};

export const KeyCombo: FC<KeyComboProps> = ({ keys }) => {
	return (
		<div className="space-x-1 inlineflex items-center">
			{keys.map(key => (
				<kbd key={key} className="relative inline-flex py-1 px-3 min-w-[1rem] max-h-8 text-white text-sm text-center font-display font-bold uppercase bg-gray-700 rounded-sm border border-gray-600 shadow-[inset_0_-4px_0_var(--color-gray-800)] cursor-default translate-y-2px active:text-gray-300 active:translate-y-[2px] active:shadow-[inset_0_-2px_0_var(--color-gray-900)] transition-all duration-100">
					<span>{key}</span>
				</kbd>
			))}
		</div>
	);
};
