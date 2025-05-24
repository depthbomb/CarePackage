import cx from 'clsx';
import Icon from '@mdi/react';
import { memo, useId, forwardRef } from 'react';
import type { HTMLAttributes } from 'react';

export type AlertProps = Omit<HTMLAttributes<HTMLElement>, 'role'> & {
	variant: 'brand' | 'success' | 'info' | 'warning' | 'danger';
	icon?: string;
	title?: string;
};

export const Alert = memo(forwardRef<HTMLButtonElement, AlertProps>(({ variant, icon, title, className, ...props }, ref) => {
	const containerCss = cx(
		'py-2 px-3 space-x-2 flex rounded-xs border shadow shadow-black/50',
		{
			'text-rose-100 bg-rose-950 border-rose-900': variant === 'brand',
			'text-green-100 bg-green-950 border-green-900': variant === 'success',
			'text-cyan-100 bg-cyan-950 border-cyan-900': variant === 'info',
			'text-yellow-100 bg-yellow-950 border-yellow-900': variant === 'warning',
			'text-red-100 bg-red-950 border-red-900': variant === 'danger',
		},
		className,
	);
	const iconCss = cx(
		'size-6',
		{
			'text-rose-500': variant === 'brand',
			'text-green-500': variant === 'success',
			'text-cyan-500': variant === 'info',
			'text-yellow-500': variant === 'warning',
			'text-red-500': variant === 'danger',
		},
	);

	return (
		<aside id={useId()} ref={ref} className={containerCss} {...props} role="alert">
			{icon && <Icon path={icon} className={iconCss}/>}
			<div className="space-y-1.5">
				{title && <h4 className="text-lg font-display font-bold">{title}</h4>}
				{props.children}
			</div>
		</aside>
	);
}));
