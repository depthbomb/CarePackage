import { atom } from 'jotai';
import { PostOperationAction } from 'shared';
import { RESET, atomWithReset } from 'jotai/utils';
import type { ISoftwareDefinition } from 'shared';

const isElevatedAtom          = atom<boolean>(false);
const isWorkingAtom           = atom<boolean>(false);
const updateAvailable         = atom<boolean>(false);
const softwareDefinitionsAtom = atom<ISoftwareDefinition[]>([]);
const selectedSoftwareAtom    = atom<ISoftwareDefinition[]>([]);
const skipInstallationAtom    = atomWithReset<boolean>(false);
const installSilentlyAtom     = atomWithReset<boolean>(false);
const cleanupAfterInstallAtom = atomWithReset<boolean>(false);
const openDownloadDirAtom     = atomWithReset<boolean>(false);
const postOperationActionAtom = atomWithReset<PostOperationAction>(PostOperationAction.DoNothing);

const resetOptionsAtom = atom(null, (_get, set) => {
	set(skipInstallationAtom, RESET);
	set(installSilentlyAtom, RESET);
	set(cleanupAfterInstallAtom, RESET);
	set(openDownloadDirAtom, RESET);
	set(postOperationActionAtom, RESET);
});

export const app = {
	isElevatedAtom,
	isWorkingAtom,
	updateAvailable,
	softwareDefinitionsAtom,
	selectedSoftwareAtom,
	skipInstallationAtom,
	installSilentlyAtom,
	cleanupAfterInstallAtom,
	openDownloadDirAtom,
	postOperationActionAtom,
	resetOptionsAtom,
} as const;
