import { atom } from 'jotai';

const showCategoryBadges = atom<boolean>(true);

export const ui = {
	showCategoryBadges
} as const;
