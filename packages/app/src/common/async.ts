/**
 * Returns a promise after the provided {@link ms} has passed
 * @param ms The number of milliseconds to wait
 */
export function timeout(ms: number) {
	return new Promise((res) => setTimeout(res, ms));
}

/**
 * Rejects a promise after the provided {@link ms} has passed
 * @param ms The number of milliseconds to wait
 */
export function rejectionTimeout(ms: number) {
	return new Promise((_, rej) => setTimeout(rej, ms));
}

export async function withTimeout<T>(promise: Promise<T>, ms: number, onTimeout?: () => void) {
	return new Promise<T>((resolve, reject) => {
		const timer = setTimeout(() => {
			onTimeout?.();
			reject(new Error(`Operation timed out after ${ms}ms`));
		}, ms);

		promise
			.then(result => {
				clearTimeout(timer);
				resolve(result);
			})
			.catch(err => {
				clearTimeout(timer);
				reject(err);
			});
	});
}
