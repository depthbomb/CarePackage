import cx from 'clsx';
import type { FC } from 'react';

type ProgressBarProps = {
	label?: string;
	value: number;
	className?: string;
};

export const ProgressBar: FC<ProgressBarProps> = ({ label, value, className, ...props }) => {
	return (
		<div className={cx('relative min-w-56 h-4 bg-gray-700 rounded-xs shadow-sm overflow-hidden', className)} {...props}>
			{label && <span className="absolute w-full font-mono text-xs text-center text-white">{label}</span>}
			<div className="h-4 bg-gradient-to-r from-rose-600 to-rose-500 transition-all" style={{ width: `${value}%` }}></div>
		</div>
	);
};
