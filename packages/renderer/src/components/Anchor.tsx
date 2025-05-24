import { memo, forwardRef } from 'react';
import type { AnchorHTMLAttributes } from 'react';

export const Anchor = memo(forwardRef<HTMLAnchorElement, AnchorHTMLAttributes<HTMLAnchorElement>>(({ className, ...props }, ref) => {
	return <a ref={ref} {...props} className={`text-rose-500 hover:text-rose-400 active:text-rose-600 ${className}`}>{props.children}</a>
}));
