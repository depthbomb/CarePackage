import { join } from 'node:path';
import { product } from 'shared';
import { Container } from '@needle-di/core';
import { MainService } from './services/main';
import { app, Menu, protocol } from 'electron';

app.setPath('userData', join(app.getPath('appData'), product.author, product.dirName));

if (import.meta.env.DEV) {
	import('@swc-node/sourcemap-support').then(({ installSourceMapSupport }) => installSourceMapSupport());
}

if (import.meta.env.PROD) {
	Menu.setApplicationMenu(null);
}

protocol.registerSchemesAsPrivileged([
	{
		scheme: 'software-icon',
		privileges: {
			supportFetchAPI: true,
			bypassCSP: true,
		}
	}
]);

app.whenReady().then(() => new Container().get(MainService).boot());
