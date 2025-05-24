import cx from 'clsx';
import { memo, useId, forwardRef } from 'react';
import type { FieldsetHTMLAttributes } from 'react';

type FieldsetProps = FieldsetHTMLAttributes<HTMLFieldSetElement>;

export const Fieldset = memo(forwardRef<HTMLFieldSetElement, FieldsetProps>(({ className, ...props }, ref) => {
	return (
		<fieldset ref={ref} id={useId()} className={cx('space-y-2 flex flex-col items-start', className)} {...props}>
			{props.children}
		</fieldset>
	);
}));
