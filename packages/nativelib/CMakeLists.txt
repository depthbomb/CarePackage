cmake_minimum_required(VERSION 3.31)
project(nativelib)

set(CMAKE_CXX_STANDARD 26)

include_directories(
        ../../node_modules/node-addon-api
        ../../node_modules/node-addon-api/napi
        "C:\\Program Files\\nodejs\\include\\node"
)

add_library(nativelib lib/nativelib.cc)
