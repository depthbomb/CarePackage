{
	"targets": [
		{
			"target_name": "nativelib",
			"sources": ["lib/nativelib.cc"],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")"
			],
			"cflags!": ["-fno-exceptions"],
			"cflags_cc!": ["-fno-exceptions"],
			"defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"]
		}
	]
}
