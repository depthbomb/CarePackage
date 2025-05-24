const { Configuration } = require('electron-builder');
const { version, author, nameLong, description, appUserModelId, applicationName } = require('../../product.json');

const isProduction = process.env.NODE_ENV === 'production';

/**
 * Whether or not to entirely skip adding node_modules to the app's asar.
 *
 * Setting this to `true` is useful in cases where third-party package code is completely bundled
 * into your compiled app code.
 */
const EXCLUDE_ALL_NODE_MODULES = true;
/**
 * Specific package names to exclude from the app's asar when `EXCLUDE_ALL_NODE_MODULES` is false.
 *
 * If a package has dependencies then you must exclude those as well.
 */
const EXCLUDED_PACKAGES = [];

/**
 * @type Configuration
 */
const config = {
	appId: appUserModelId,
	executableName: applicationName,
	productName: nameLong,
	copyright: `Copyright © 2024-${new Date().getFullYear()} ${author}`,
	asar: true,
	buildDependenciesFromSource: true,
	compression: 'maximum',
	directories: {
		output: '../../build'
	},
	files: [
		'dist/*',
		'package.json',
	],
	asarUnpack: [
		'*.node',
		'*.dll',
		'*.exe',
	],
	extraMetadata: {
		version,
		description
	},
	extraFiles: [
		{
			from: '../../static/extra/carepackage.VisualElementsManifest.xml',
			to: 'carepackage.VisualElementsManifest.xml'
		},
		{
			from: '../../static/extra/bin/aria2c.exe',
			to: 'bin/aria2c.exe'
		},
	],
	extraResources: [
		{
			from: '../../static/extra/software-icons',
			to: 'software-icons',
			filter: ['**/*.png']
		},
		{
			from: '../../static/extra/Square70x70Logo.png',
			to: 'Square70x70Logo.png',
		},
		{
			from: '../../static/extra/Square150x150Logo.png',
			to: 'Square150x150Logo.png',
		},
		{ from: '../nativelib/build/Release/nativelib.node', to: 'native/nativelib.node' },
	],
	win: {
		icon: '../../static/icon.ico',
		signtoolOptions: {
			publisherName: author
		},
	},
	electronFuses: {
		runAsNode: !isProduction,
		onlyLoadAppFromAsar: isProduction,
		enableCookieEncryption: isProduction,
		enableNodeCliInspectArguments: !isProduction,
		enableNodeOptionsEnvironmentVariable: !isProduction,
		enableEmbeddedAsarIntegrityValidation: isProduction,
	}
};

if (EXCLUDE_ALL_NODE_MODULES) {
	config.files.push('!node_modules');
} else {
	for (const excludedPackage of EXCLUDED_PACKAGES) {
		config.files.push(`!node_modules/${excludedPackage}`);
	}
}

exports.default = config;
