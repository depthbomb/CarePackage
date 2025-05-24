import { DEV_PORT } from 'shared';
import { resolve } from 'node:path';
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react-swc';
import { URL, fileURLToPath } from 'node:url';
import type { UserConfigExport } from 'vite';

export default defineConfig(({ mode }) => {
	const isProduction = mode === 'production';
	const config: UserConfigExport = {
		root: resolve('./src'),
		base: '',
		build: {
			outDir: isProduction ? resolve('../app/dist') : resolve('./dist'),
			assetsDir: '.',
			emptyOutDir: false,
			sourcemap: mode !== 'production',
			minify: isProduction ? 'terser' : false,
			assetsInlineLimit: (path, content) => path.endsWith('.svg') || content.byteLength <= 100,
			rollupOptions: {
				input: {
					index: resolve('./src/index.html'),
				},
				output: {
					entryFileNames: '[hash].js',
					assetFileNames: '[hash].[ext]',
					chunkFileNames: '[hash].js',
				},
			}
		},
		plugins: [
			react(),
			tailwindcss()
		],
		resolve: {
			alias: {
				'~': fileURLToPath(new URL('./src', import.meta.url))
			}
		},
	};

	if (mode !== 'production') {
		config.server = {
			port: DEV_PORT
		};
	}

	return config;
});
