import semver from 'semver';
import { product, IpcChannel } from 'shared';
import { WindowService } from '~/services/window';
import { GithubService } from '~/services/github';
import { REPO_NAME, REPO_OWNER } from '~/constants';
import { inject, injectable } from '@needle-di/core';
import { LifecycleService } from '~/services/lifecycle';
import type { Maybe } from 'shared';
import type { IBootstrappable } from '~/common/IBootstrappable';

@injectable()
export class UpdaterService implements IBootstrappable {
	private isNotified = false;
	private checkInterval: Maybe<NodeJS.Timeout>;

	public constructor(
		private readonly lifecycle = inject(LifecycleService),
		private readonly window    = inject(WindowService),
		private readonly github    = inject(GithubService),
	) {}

	public async bootstrap() {
		this.checkInterval = setInterval(async () => await this.checkForUpdates(), 180_000);

		this.lifecycle.events.on('readyPhase', async () => await this.checkForUpdates());
		this.lifecycle.events.on('shutdown',   () => clearInterval(this.checkInterval));
	}

	public async checkForUpdates() {
		this.window.emitAll(IpcChannel.Updater_CheckingForUpdates);

		try {
			const releases   = await this.github.getRepositoryReleases(REPO_OWNER, REPO_NAME);
			const newRelease = releases.find(r => {
				const remoteVersion = semver.coerce(r.tag_name);
				return remoteVersion && semver.gt(remoteVersion, product.version);
			});

			if (newRelease && !this.isNotified) {
				this.window.emitMain(IpcChannel.Updater_Outdated);
				this.isNotified = true;
			}
		} catch (err) {
			console.error(err);
		}
	}
}
