import cx from 'clsx';
import { baseCss } from './baseCss';
import { memo, forwardRef } from 'react';
import type { InputHTMLAttributes } from 'react';

type InputProps = InputHTMLAttributes<HTMLInputElement>;

export const Input = memo(forwardRef<HTMLInputElement, InputProps>(({ className, ...props }, ref) => {
	const css = cx(baseCss, 'read-only:text-gray-400', 'read-only:cursor-default', className);

	return (
		<input ref={ref} className={css} {...props}/>
	);
}));
