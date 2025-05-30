import { memo, forwardRef } from 'react';
import type { AnchorHTMLAttributes } from 'react';

export const Anchor = memo(forwardRef<HTMLAnchorElement, AnchorHTMLAttributes<HTMLAnchorElement>>(({ className, ...props }, ref) => {
	return <a ref={ref} {...props} className={`text-accent-500 hover:text-accent-400 active:text-accent-600 underline underline-offset-3 hover:no-underline ${className}`}>{props.children}</a>
}));
