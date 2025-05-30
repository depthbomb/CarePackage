import cx from 'clsx';
import { useId } from 'react';
import { Switch as SwitchPrimitive } from 'radix-ui';
import type { FC } from 'react';

type SwitchProps = SwitchPrimitive.SwitchProps & {
	label?: string;
};

export const Switch: FC<SwitchProps> = ({ label, checked, ...props }) => {
	return (
		<div id={useId()} className="space-x-3 flex items-center">
			<SwitchPrimitive.Root checked={checked} className={cx('relative h-6 w-12 cursor-default rounded-xs bg-gray-600 outline-none data-[state=checked]:bg-accent-500 transition-colors disabled:opacity-50! disabled:cursor-not-allowed!')} {...props}>
				<SwitchPrimitive.Thumb className="block size-5 translate-x-0.5 bg-white data-[state=checked]:bg-accent-foreground rounded-xs transition-all will-change-transform data-[state=checked]:translate-x-6.5" />
			</SwitchPrimitive.Root>
			{label && <span>{label}</span>}
		</div>
	);
};
