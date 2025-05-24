import { spawn } from 'node:child_process';
import { injectable } from '@needle-di/core';
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

		return new Promise<number>((res, rej) => {
			let child: ChildProcess;
			if (exePath.endsWith('.msi')) {
				child = spawn('cmd.exe', ['/c', exePath, ...args]);
			} else {
				child = spawn(exePath, args);
			}

			child.once('exit', code => {
				console.log('process', exePath, 'exited with code', code);
				res(code as number);
			});
			child.once('error', err => {
				console.log('error executing process', exePath, '-', err);
				rej(err);
			});
		});
	}
}
