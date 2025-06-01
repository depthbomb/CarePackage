import { useMemo } from 'react';

function getValueFromPath<T>(obj: any, path: string): T | undefined {
	return path.split('.').reduce((acc, part) => acc?.[part], obj);
}

export const useConfig = () => {
	const config = useMemo(() => {
		const searchParams = new URLSearchParams(window.location.search);
		const configParam = searchParams.get('config');
		if (!configParam) return {};

		try {
			return JSON.parse(configParam);
		} catch {
			return {};
		}
	}, []);

	const getConfigValue = <T = any>(path: string): T | undefined => {
		return getValueFromPath<T>(config, path);
	}

	return getConfigValue;
}
