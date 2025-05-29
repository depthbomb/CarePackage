import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'rustup';
	public name = 'Rustup';
	public category = [SoftwareCategory.Development];
	public downloadName = 'rustup-init.exe';
	public icon = 'rust.png';
	public homepage = 'https://rust-lang.org/learn/get-started';

	public async resolveDownloadUrl() {
		return ok('https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe');
	}
}
