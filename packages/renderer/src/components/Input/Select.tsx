import cx from 'clsx';
import { forwardRef } from 'react';
import { baseCss } from './baseCss';
import type { SelectHTMLAttributes } from 'react';

type SelectProps = Omit<SelectHTMLAttributes<HTMLSelectElement>, 'size'>;

export const Select = forwardRef<HTMLSelectElement, SelectProps>(({ className, children, ...props }, ref) => {
	const css = cx(baseCss, 'disabled:opacity-50! disabled:cursor-not-allowed!', className);

	return (
		<select ref={ref} className={css} {...props}>
			{children}
		</select>
	);
});
