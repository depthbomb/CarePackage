import { Socket } from 'node:net';

export function findFreePort(startPort: number, maxAttempts: number, timeout: number, stride: number = 1) {
	let done = false;

	return new Promise<number>(res => {
		const timeoutHandle = setTimeout(() => {
			if (!done) {
				done = true;
				return res(0);
			}
		}, timeout);

		doFindFreePort(startPort, maxAttempts, stride, port => {
			if (!done) {
				done = true;
				clearTimeout(timeoutHandle);
				return res(port);
			}
		});
	});
}

function doFindFreePort(startPort: number, maxAttempts: number, stride: number, cb: (port: number) => void) {
	if (maxAttempts === 0) {
		return cb(0);
	}

	const client = new Socket();
	client.once('connect', () => {
		dispose(client);

		return doFindFreePort(startPort + stride, maxAttempts - 1, stride, cb);
	});
	client.once('error', (err: Error & { code?: string }) => {
		dispose(client);

		if (err.code !== 'ECONNREFUSED') {
			return doFindFreePort(startPort + stride, maxAttempts - 1, stride, cb);
		}

		return cb(startPort);
	});

	client.connect(startPort, '127.0.0.1');
}

function dispose(socket: Socket): void {
	try {
		socket.removeAllListeners('connect');
		socket.removeAllListeners('error');
		socket.end();
		socket.destroy();
		socket.unref();
	} catch (error) {
		console.error(error);
	}
}
