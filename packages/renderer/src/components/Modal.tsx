import cx from 'clsx/lite';
import Icon from '@mdi/react';
import { mdiClose } from '@mdi/js';
import { createPortal } from 'react-dom';
import { useId, useRef, useState, useEffect, forwardRef, cloneElement, useImperativeHandle } from 'react';
import type { JSX, ReactNode } from 'react';

export type ModalProps = {
	title: JSX.Element;
	trigger?: JSX.Element;
	shown?: boolean;
	onVisibilityChange?: (visible: boolean) => void;
	canClose?: boolean;
	showCloseIcon?: boolean;
	children: ReactNode;
	footer?: JSX.Element;
	portalId?: string;
};

export type ModalHandle = {
	closeModal: () => void;
};

const overlayBaseCss = 'absolute inset-0 m-auto w-[calc(100vw-2px)] h-[calc(100vh-2px)] flex items-center justify-center bg-black/66 backdrop-blur-[2px] backdrop-grayscale-100 opacity-0 -z-10 transition-[opacity,backdrop-filter] duration-250' as const;

const contentBaseCss = 'w-2/3 h-3/4 flex flex-col bg-gray-900 rounded-xs border border-gray-700 shadow-lg shadow-black/50 opacity-0 scale-[0.95] transition-all duration-250' as const;

export const Modal = forwardRef<ModalHandle, ModalProps>(({
	title,
	trigger,
	shown = false,
	onVisibilityChange,
	canClose = true,
	showCloseIcon = true,
	children,
	footer,
	portalId = 'portal',
}, ref) => {
	const key = useId();
	const [isVisible, setIsVisible] = useState(false);

	const triggerElement = useRef(
		!!trigger &&
			cloneElement(trigger, {
				id: key,
				onClick: () => onVisibilityChange?.(true),
			})
	);

	const contentCss = cx(contentBaseCss, isVisible && 'scale-[1] opacity-100');
	const overlayCss = cx(overlayBaseCss, isVisible && 'opacity-100');

	const closeModal = () => {
		if (!canClose) return;

		setIsVisible(false);
		setTimeout(() => onVisibilityChange?.(false), 250);
	};

	useImperativeHandle(ref, () => ({ closeModal }));

	useEffect(() => {
		setTimeout(() => setIsVisible(shown), 0);
	}, [shown]);

	return (
		<>
			{triggerElement.current}
			{shown &&
				createPortal(
					<div
						id={`modal-${key}`}
						className="absolute inset-0 flex items-center justify-center z-[9001]"
					>
						<div className={contentCss}>
							<div className="p-3 w-full flex items-center shrink-0 border-b border-gray-700">
								{title}
								{showCloseIcon && canClose && (
									<button
										onClick={closeModal}
										className="ml-auto size-6 flex items-center justify-center text-gray-400 hover:text-white rounded-xs transition-colors"
										type="button"
									>
										<Icon path={mdiClose} className="size-5" />
									</button>
								)}
							</div>
							<div className="p-3 overflow-y-auto [scrollbar-width:thin]">
								{children}
							</div>
							{footer}
						</div>
						<div onClick={closeModal} className={overlayCss} />
					</div>,
					document.getElementById(portalId)!,
					key
				)}
		</>
	);
});
