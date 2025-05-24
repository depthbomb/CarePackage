export async function wait(duration: number) {
	return new Promise(res => setTimeout(res, duration));
}

export async function pollUntil(fn: () => boolean, duration: number = 1_000) {
	while (!fn()) {
		await wait(duration);
	}
}

export function isNumber(input: unknown): input is number {
	return (typeof input === 'number' && !isNaN(input));
}

// Adapted from https://github.com/microsoft/vscode/blob/18ed64835ec8f8227dbd8562d2d9fd9fa339abbb/src/vs/platform/files/common/files.ts#L1534
export class ByteSize {
	public static readonly KB = 1024;
	public static readonly MB = ByteSize.KB * ByteSize.KB;
	public static readonly GB = ByteSize.MB * ByteSize.KB;
	public static readonly TB = ByteSize.GB * ByteSize.KB;

	public static formatSize(size: number): string {
		if (!isNumber(size)) {
			size = 0;
		}

		if (size < ByteSize.KB) {
			return `${size.toFixed(0)}B`;
		}

		if (size < ByteSize.MB) {
			return `${(size / ByteSize.KB).toFixed(2)}KB`;
		}

		if (size < ByteSize.GB) {
			return `${(size / ByteSize.MB).toFixed(2)}MB`;
		}

		if (size < ByteSize.TB) {
			return `${(size / ByteSize.GB).toFixed(2)}GB`;
		}

		return `${(size / ByteSize.TB).toFixed(2)}TB`;
	}
}
