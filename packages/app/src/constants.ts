import { app } from 'electron';
import { join, dirname } from 'node:path';
import { product, GIT_HASH_SHORT } from 'shared';

export const REPO_OWNER = 'depthbomb' as const;
export const REPO_NAME  = 'CarePackage' as const;

export const ROOT_PATH = __dirname;
/**
 * This constant is for development use only. **DO NOT** use it or any other constant that uses it
 * in production as it may not return an expected value.
 */
export const MONOREPO_ROOT_PATH = join(process.cwd(), '..', '..');
export const EXE_PATH           = app.getPath('exe');
export const EXE_DIR            = dirname(EXE_PATH);
export const RESOURCES_PATH     = join(EXE_DIR, 'resources');
export const PRELOAD_PATH       = join(ROOT_PATH, 'preload.js');
export const DOWNLOAD_DIR       = join(app.getPath('temp'), `.${product.applicationName}`);

export const USER_AGENT         = `CarePackage/${product.version}+${GIT_HASH_SHORT} (github:${REPO_OWNER}/${REPO_NAME})` as const;
export const BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' as const;

/**
 * Hosts that can be opened in an external browser from the renderer.
 */
export const EXTERNAL_HOSTS_WHITELIST = [
	'github.com',
	'ninite.com',
];
