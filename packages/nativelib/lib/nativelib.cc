#include <string>
#include <napi.h>
#include <windows.h>
#include <shellapi.h>

bool EnableShutdownPrivilege() {
    HANDLE hToken;
    TOKEN_PRIVILEGES tkp;

    if (!OpenProcessToken(GetCurrentProcess(), TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY, &hToken)) {
        return false;
    }

    LookupPrivilegeValue(nullptr, SE_SHUTDOWN_NAME, &tkp.Privileges[0].Luid);

    tkp.PrivilegeCount = 1;
    tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED;

    const BOOL result = AdjustTokenPrivileges(hToken, FALSE, &tkp, 0, nullptr, nullptr);
    CloseHandle(hToken);

    return result && GetLastError() == ERROR_SUCCESS;
}

Napi::Value ExitWindowsWrapped(const Napi::CallbackInfo& info) {
    const Napi::Env env = info.Env();

    if (!ExitWindowsEx(0, 0)) {
        Napi::Error::New(env, "Failed to exit Windows").ThrowAsJavaScriptException();
    }

    return env.Undefined();
}

Napi::Value LockWorkStationWrapped(const Napi::CallbackInfo& info) {
    const Napi::Env env = info.Env();

    if (!LockWorkStation()) {
        Napi::Error::New(env, "Failed to lock workstation").ThrowAsJavaScriptException();
    }

    return env.Undefined();
}

Napi::Value ScheduleShutdownWrapped(const Napi::CallbackInfo& info) {
    const Napi::Env env = info.Env();

    if (info.Length() < 4 ||
        !info[0].IsNumber() ||
        !info[1].IsString() ||
        !info[2].IsBoolean() ||
        !info[3].IsBoolean()) {
        Napi::TypeError::New(env, "Expected arguments: (delaySeconds: number, message: string, reboot: boolean, force: boolean)").ThrowAsJavaScriptException();
        return env.Null();
    }

    const int delaySeconds = info[0].As<Napi::Number>().Int32Value();
    std::string messageUtf8 = info[1].As<Napi::String>().Utf8Value();
    const bool reboot = info[2].As<Napi::Boolean>().Value();
    const bool force = info[3].As<Napi::Boolean>().Value();

    const std::wstring messageW(messageUtf8.begin(), messageUtf8.end());

    LPWSTR messagePtr = nullptr;
    if (!messageW.empty()) {
        messagePtr = new wchar_t[messageW.length() + 1];
        wcscpy_s(messagePtr, messageW.length() + 1, messageW.c_str());
    }

    if (!EnableShutdownPrivilege()) {
        delete[] messagePtr;
        Napi::Error::New(env, "Failed to enable shutdown privilege").ThrowAsJavaScriptException();
        return env.Null();
    }

    const BOOL result = InitiateSystemShutdownExW(
        nullptr,
        messagePtr,
        delaySeconds,
        force ? TRUE : FALSE,
        reboot ? TRUE : FALSE,
        SHTDN_REASON_MAJOR_APPLICATION | SHTDN_REASON_MINOR_INSTALLATION | SHTDN_REASON_FLAG_PLANNED
    );

    delete[] messagePtr;

    if (!result) {
        const DWORD error = GetLastError();
        Napi::Error::New(env, "InitiateSystemShutdownExW failed with error: " + std::to_string(error)).ThrowAsJavaScriptException();
    }

    return env.Undefined();
}

Napi::Value IsElevatedWrapped(const Napi::CallbackInfo& info) {
    const Napi::Env env = info.Env();

    HANDLE hToken = nullptr;
    if (!OpenProcessToken(GetCurrentProcess(), TOKEN_QUERY, &hToken)) {
        Napi::Error::New(env, "Failed to open process token").ThrowAsJavaScriptException();
        return env.Null();
    }

    TOKEN_ELEVATION elevation;
    DWORD dwSize = sizeof(TOKEN_ELEVATION);

    const BOOL success = GetTokenInformation(
        hToken,
        TokenElevation,
        &elevation,
        sizeof(elevation),
        &dwSize
    );

    CloseHandle(hToken);

    if (!success) {
        Napi::Error::New(env, "Failed to get token information").ThrowAsJavaScriptException();
        return env.Null();
    }

    return Napi::Boolean::New(env, elevation.TokenIsElevated != 0);
}

Napi::Value RunAsAdminWrapped(const Napi::CallbackInfo& info) {
    const Napi::Env env = info.Env();

    if (info.Length() < 2 || !info[0].IsString() || !info[1].IsArray()) {
        Napi::TypeError::New(env, "Expected arguments: (path: string, args: string[])").ThrowAsJavaScriptException();
        return env.Null();
    }

    std::string exePathUtf8 = info[0].As<Napi::String>().Utf8Value();
    const std::wstring exePathW(exePathUtf8.begin(), exePathUtf8.end());

    const auto argsArray = info[1].As<Napi::Array>();
    std::wstring argumentsW;

    for (uint32_t i = 0; i < argsArray.Length(); ++i) {
        if (!argsArray.Get(i).IsString()) {
            Napi::TypeError::New(env, "All arguments in args array must be strings").ThrowAsJavaScriptException();
            return env.Null();
        }

        std::string argUtf8 = argsArray.Get(i).As<Napi::String>().Utf8Value();
        const std::wstring argW(argUtf8.begin(), argUtf8.end());

        if (!argumentsW.empty()) {
            argumentsW += L" ";
        }

        argumentsW += argW;
    }

    HINSTANCE result = ShellExecuteW(
        nullptr,
        L"runas",               // Run as admin
        exePathW.c_str(),       // Executable path
        argumentsW.c_str(),     // Arguments
        nullptr,                // Default directory
        SW_SHOWNORMAL           // Show the window normally
    );

    if (reinterpret_cast<INT_PTR>(result) <= 32) {
        Napi::Error::New(env, "Failed to launch process as admin, error code: " + std::to_string(reinterpret_cast<INT_PTR>(result))).ThrowAsJavaScriptException();
        return env.Null();
    }

    return env.Undefined();
}

Napi::Object Init(const Napi::Env env, const Napi::Object exports) {
    exports.Set(Napi::String::New(env, "exitWindows"), Napi::Function::New(env, ExitWindowsWrapped));
    exports.Set(Napi::String::New(env, "lockWorkStation"), Napi::Function::New(env, LockWorkStationWrapped));
    exports.Set(Napi::String::New(env, "scheduleShutdown"), Napi::Function::New(env, ScheduleShutdownWrapped));
    exports.Set(Napi::String::New(env, "isElevated"), Napi::Function::New(env, IsElevatedWrapped));
    exports.Set(Napi::String::New(env, "runAsAdmin"), Napi::Function::New(env, RunAsAdminWrapped));
    return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
