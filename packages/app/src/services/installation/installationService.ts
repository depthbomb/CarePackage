import { x } from 'tinyexec';
import { injectable } from '@needle-di/core';
import type { Output } from 'tinyexec';
import type { ChildProcess } from 'node:child_process';

@injectable()
export class InstallationService {
	private readonly silentArgs: string[];

	public constructor() {
		this.silentArgs = [
			'--silent',
			'--no-interaction',
			'--no-input',
			'--no-user-input',
			'--quiet',
			'--passive',
			'/quiet',
			'/passive',
			'/silent',
			'/q',
			'/S',
			'/s'
		];
	}

	public async runExecutable(exePath: string, silent: boolean) {
		const args: string[] = [];
		if (silent) {
			args.push(...this.silentArgs);
		}

		let proc: Output;
		if (exePath.endsWith('.msi')) {
			proc = await x('cmd.exe', ['/c', exePath, ...args]);
		} else {
			proc = await x(exePath, args);
		}

		return proc.exitCode ?? 0;
	}
}
