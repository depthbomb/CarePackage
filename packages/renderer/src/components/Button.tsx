import cx from 'clsx';
import { memo, forwardRef } from 'react';
import type { ButtonHTMLAttributes } from 'react';

export type ButtonProps = Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'type'> & {
	variant?: 'normal' | 'brand' | 'success' | 'info' | 'warning' | 'danger';
	size?: 'sm' | 'lg' | 'xl';
};

const baseCss = 'flex items-center justify-center font-semibold shadow transition-colors cursor-pointer disabled:opacity-50! disabled:pointer-events-none!' as const;

export const Button = memo(forwardRef<HTMLButtonElement, ButtonProps>(({ variant, size, className, ...props }, ref) => {
	const css = cx(
		baseCss,
		{
			// Variant classes
			'text-white bg-gray-700 hover:bg-gray-600 active:bg-gray-800': variant === 'normal' || !variant,
			'text-white bg-rose-500 hover:bg-rose-400 active:bg-rose-600': variant === 'brand',
			'text-green-50 bg-green-500 hover:bg-green-600 active:bg-green-700': variant === 'success',
			'text-cyan-950 bg-cyan-500 hover:bg-cyan-600 active:bg-cyan-700': variant === 'info',
			'text-orange-50 bg-orange-500 hover:bg-orange-600 active:bg-orange-700': variant === 'warning',
			'text-red-100 bg-red-500 hover:bg-red-400 active:bg-red-600': variant === 'danger',
			// Size classes
			'px-2 space-x-1 h-6 text-xs rounded-xs': size === 'sm',
			'px-2.5 space-x-1 text-sm h-7.5 rounded-xs': !size,
			'px-3 space-x-1.5 h-8 rounded-sm': size === 'lg',
			'px-4 space-x-1.5 h-9.5 text-xl rounded-sm': size === 'xl',
		},
		className
	);

	return (
		<button
			ref={ref}
			className={css}
			{...props}
			type="button"
		>{props.children}</button>
	);
}));
