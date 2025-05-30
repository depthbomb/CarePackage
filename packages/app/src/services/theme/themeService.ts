import { systemPreferences } from 'electron';
import { WindowService } from '~/services/window';
import { inject, injectable } from '@needle-di/core';
import type { BrowserWindow } from 'electron';
import type { IBootstrappable } from '~/common/IBootstrappable';

const SYSTEM_PREFERENCES_COLORS = [
	'3d-dark-shadow',
	'3d-face',
	'3d-highlight',
	'3d-light',
	'3d-shadow',
	'active-border',
	'active-caption',
	'active-caption-gradient',
	'app-workspace',
	'button-text',
	'caption-text',
	'desktop',
	'disabled-text',
	'highlight',
	'highlight-text',
	'hotlight',
	'inactive-border',
	'inactive-caption',
	'inactive-caption-gradient',
	'inactive-caption-text',
	'info-background',
	'info-text',
	'menu',
	'menu-highlight',
	'menubar',
	'menu-text',
	'scrollbar',
	'window',
	'window-frame',
	'window-text',
	'control-background',
	'control',
	'control-text',
	'disabled-control-text',
	'find-highlight',
	'grid',
	'header-text',
	'highlight',
	'keyboard-focus-indicator',
	'label',
	'link',
	'placeholder-text',
	'quaternary-label',
	'scrubber-textured-background',
	'secondary-label',
	'selected-content-background',
	'selected-control',
	'selected-control-text',
	'selected-menu-item-text',
	'selected-text-background',
	'selected-text',
	'separator',
	'shadow',
	'tertiary-label',
	'text-background',
	'text',
	'under-page-background',
	'unemphasized-selected-content-background',
	'unemphasized-selected-text-background',
	'unemphasized-selected-text',
	'window-background',
	'window-frame-text'
] as const;

@injectable()
export class ThemeService implements IBootstrappable {
	private readonly injectedCss: Set<string>;
	private readonly systemColorKeys: typeof SYSTEM_PREFERENCES_COLORS;

	public constructor(
		private readonly window = inject(WindowService),
	) {
		this.injectedCss = new Set();
		this.systemColorKeys = SYSTEM_PREFERENCES_COLORS;
	}

	public async bootstrap() {
		systemPreferences.addListener('accent-color-changed', async () => {
			await this.removeInjectedThemeCss();
			await this.injectThemeCss();
		});

		this.window.events.on('windowCreated', this.injectThemeCssIntoWindow.bind(this));
	}

	public async injectThemeCss(): Promise<void> {
		for (const window of this.window.windows.values()) {
			const key = await window.webContents.insertCSS(this.getThemeClasses());

			this.injectedCss.add(key);
		}
	}

	public async removeInjectedThemeCss() {
		for (const window of this.window.windows.values()) {
			for (const key of this.injectedCss) {
				await window.webContents.removeInsertedCSS(key);
				this.injectedCss.delete(key);
			}
		}
	}

	public async injectThemeCssIntoWindow(window: BrowserWindow) {
		const key = await window.webContents.insertCSS(this.getThemeClasses());

		this.injectedCss.add(key);
	}

	private getThemeClasses() {
		return this.systemColorKeys.map(k => {
			try {
				return `:root,html,body {--os-accent: #${systemPreferences.getAccentColor()};--os-${k}: ${systemPreferences.getColor(k)} };`;
			} catch {
				return '';
			}
		}).join('\n');
	}
}
