import { typeFlag } from 'type-flag';
import { injectable } from '@needle-di/core';

@injectable()
export class CliService {
	public readonly args;
	public readonly flags;

	public constructor() {
		this.args = typeFlag({
			autostart: {
				type: Boolean,
				default: false
			},
			software: {
				type: String,
				default: null,
			}
		}, process.argv);
		this.flags = this.args.flags;
	}
}
