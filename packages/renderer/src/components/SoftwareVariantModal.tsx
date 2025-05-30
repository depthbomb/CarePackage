import cx from 'clsx/lite';
import { useAtom } from 'jotai';
import { app } from '~/atoms/app';
import { Button } from './Button';
import { useRef, forwardRef } from 'react';
import { Modal } from '~/components/Modal';
import type { ISoftwareDefinition } from 'shared';
import type { FC, ButtonHTMLAttributes } from 'react';
import type { ModalProps, ModalHandle } from '~/components/Modal';

import uacIcon from '~/assets/img/uac.png';
import zipIcon from '~/assets/img/zip.png';

type SoftwareVariantModalProps = Omit<ModalProps, 'title' | 'canClose' | 'children'> & {
	software: ISoftwareDefinition;
};

type SoftwareVariantButtonProps = Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'className' | 'type'> & {
	variant: ISoftwareDefinition;
	selected: boolean;
};

const SoftwareVariantButton = forwardRef<HTMLButtonElement, SoftwareVariantButtonProps>(({ variant, selected = false, ...props }, ref) => {
	return (
		<button
			ref={ref}
			className={cx('p-3 space-x-3 flex items-center', selected ? 'font-bold text-accent-foreground bg-gradient-to-r from bg-accent-500 to-gray-950' : 'hover:bg-gray-800')}
			{...props}
			type="button"
		>
			<img src={`software-icon://${variant.icon}`} className="size-8" width="32" height="32" draggable="false"/>
			<span className="text-lg font-display">{variant.name}</span>
			{variant.requiresAdmin && <img className="size-4" src={uacIcon} width="16" height="16" draggable="false"/>}
			{variant.isArchive && <img className="size-4" src={zipIcon} width="16" height="16" draggable="false"/>}
		</button>
	);
});

export const SoftwareVariantModal: FC<SoftwareVariantModalProps> = ({
	shown,
	onVisibilityChange,
	software,
	...props
}) => {
	const modalRef                                = useRef<ModalHandle>(null);
	const variants                                = useRef(software.variants!);
	const [selectedSoftware, setSelectedSoftware] = useAtom(app.selectedSoftwareAtom);

	const hasVariantsSelected = variants.current.some(v => selectedSoftware.some(sw => sw.key === v.key));

	const onSoftwareVariantButtonClicked = (variant: ISoftwareDefinition) => {
		setSelectedSoftware(prev => {
			const isAlreadySelected = prev.some(sw => sw.key === variant.key);
			if (isAlreadySelected) {
				return prev.filter(sw => sw.key !== variant.key);
			} else {
				return [...prev, variant];
			}
		});
	};

	const onCancelButtonClicked = () => {
		setSelectedSoftware(prev =>
			prev.filter(sw => !variants.current.some(v => v.key === sw.key))
		);

		modalRef.current?.closeModal(true);
	};

	const onContinueButtonClicked = () => {
		modalRef.current?.closeModal(true);
	};

	return (
		<Modal
			ref={modalRef}
			canClose={false}
			shown={shown}
			onVisibilityChange={onVisibilityChange}
			title={
				<div className="space-x-1 flex items-center text-gray-400">
					<h1 className="font-display font-bold text-xl">{software.name}</h1>
				</div>
			}
			footer={
				<div className="p-3 space-x-2 flex items-center justify-end border-t border-gray-700">
					<Button onClick={onCancelButtonClicked}>Cancel</Button>
					<Button onClick={onContinueButtonClicked} variant="accent" disabled={!hasVariantsSelected}>Continue</Button>
				</div>
			}
			{...props}>
			<div className="flex flex-col">
				{variants.current.map(v => (
					<SoftwareVariantButton
						key={v.key}
						variant={v}
						selected={selectedSoftware.some(sw => sw.key === v.key)}
						onClick={() => onSoftwareVariantButtonClicked(v)}/>
				))}
			</div>
		</Modal>
	);
};
