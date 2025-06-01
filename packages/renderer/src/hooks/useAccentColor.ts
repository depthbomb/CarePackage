import chroma from 'chroma-js';
import { useEffect, useRef } from 'react';
import { getPalette } from 'tailwindcss-palette-generator/getPalette';

const shades = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950];

function getForegroundColor(baseColor: string) {
	const color = chroma(baseColor);
	return color.luminance() > 0.5 ? '#000' : '#fff';
}

export const useAccentColor = () => {
	const prevAccent = useRef<string | null>(null);

	useEffect(() => {
		const root = document.documentElement;

		const update = () => {
			const baseColor = getComputedStyle(root).getPropertyValue('--os-accent').trim();
			if (!baseColor || baseColor === prevAccent.current) {
				return;
			}

			prevAccent.current = baseColor;

			const fg      = getForegroundColor(baseColor);
			const palette = getPalette([
				{
					name: 'accent',
					color: baseColor,
					shades,
				},
			]) as unknown as { accent: { [shade: number]: string } };

			for (const shade of shades) {
				root.style.setProperty(`--accent-${shade}`, palette.accent[shade]);
			}

			root.style.setProperty('--accent-foreground', fg);
		};

		update();

		const interval = setInterval(update, 5_000);

		return () => clearInterval(interval);
	}, []);
}
