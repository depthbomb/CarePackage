import { useEffect } from 'react';
import type { DependencyList } from 'react';

export type AsyncEffectCallback = () => Promise<void | (() => void)>;

export const useAsyncEffect = (effect: AsyncEffectCallback, dependencies?: DependencyList): void => {
	useEffect(() => {
		const ret = effect();
		if (typeof ret === "function") {
			return ret;
		}

		ret.then(cleanup => {
			if (cleanup) {
				cleanup();
			}
		});

		return;
	}, dependencies);
}
