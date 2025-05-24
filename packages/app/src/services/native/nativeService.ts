import { join } from 'node:path';
import { injectable } from '@needle-di/core';
import { getExtraResourcePath } from '~/utils';
import { MONOREPO_ROOT_PATH } from '~/constants';

@injectable()
export class NativeService {
	private readonly nativeLib;

	public constructor() {
		if (import.meta.env.DEV) {
			this.nativeLib = require(
				join(MONOREPO_ROOT_PATH, 'packages', 'nativelib', 'build', 'Release', 'nativelib.node')
			);
		} else {
			this.nativeLib = require(
				getExtraResourcePath('native/nativelib.node')
			);
		}
	}

	public logOut(): void {
		return this.nativeLib.exitWindows();
	}

	public lock(): void {
		return this.nativeLib.lockWorkstation();
	}

	public scheduleShutdown(delay: number, message: string, reboot: boolean, forceCloseApplications: boolean): void {
		return this.nativeLib.scheduleShutdown(delay, message, reboot, forceCloseApplications);
	}

	public isElevated(): boolean {
		return this.nativeLib.isElevated();
	}
}
