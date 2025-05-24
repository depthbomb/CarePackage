import { resolve } from 'node:path';
import { defineConfig } from 'vite';
import { builtinModules } from 'module';
import type { UserConfigExport } from 'vite';

const { platform } = process;

export default defineConfig(({ mode }) => {
	const isProduction = mode === 'production';
	const config: UserConfigExport = {
		root: resolve('./src'),
		base: '',
		assetsInclude: '**/*.node',
		build: {
			target: 'node22',
			outDir: resolve('./dist'),
			assetsDir: '.',
			emptyOutDir: true,
			sourcemap: !isProduction,
			minify: isProduction ? 'terser' : false,
			lib: {
				entry: {
					app: resolve('./src/index.ts'),
					preload: resolve('./src/preload.ts'),
				},
				formats: ['cjs']
			},
			rollupOptions: {
				output: {
					entryFileNames: '[name].js',
					assetFileNames: '[hash].[ext]',
					chunkFileNames: '[hash].js',
				},
				external: [
					'electron',
					'original-fs',
					'node:original-fs',
					...builtinModules.flatMap(p => [p, `node:${p}`]),
				]
			},
			terserOptions: {
				format: {
					comments: false
				}
			},
		},
		define: {
			__WIN32__: platform === 'win32',
			__MACOS__: platform === 'darwin',
			__LINUX__: platform === 'linux',
			__STRICT__: isProduction,
			__BUILD_DATE__: new Date(),
		},
		resolve: {
			alias: {
				'~': resolve('./src'),
			}
		},
	};

	return config;
});
