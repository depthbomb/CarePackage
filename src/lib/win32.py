from PySide6.QtWidgets import QWidget, QApplication
from winreg import OpenKey, CloseKey, QueryValueEx, ConnectRegistry, HKEY_CURRENT_USER
from ctypes import c_int, byref, c_bool, windll, HRESULT, wintypes, c_wchar_p, Structure

user32 = windll.user32
advapi32 = windll.advapi32
dwmapi = windll.dwmapi
shell32 = windll.shell32
kernel32 = windll.kernel32

TOKEN_ADJUST_PRIVILEGES = 0x0020
TOKEN_QUERY = 0x0008
SE_PRIVILEGE_ENABLED = 0x00000002
ERROR_SUCCESS = 0

SHTDN_REASON_MAJOR_APPLICATION = 0x00040000
SHTDN_REASON_MINOR_INSTALLATION = 0x00000002
SHTDN_REASON_FLAG_PLANNED = 0x80000000

DWM_BB_ENABLE = 0x00000001
DWM_BB_BLURREGION = 0x00000002
DWM_BB_TRANSITIONONMAXIMIZED = 0x00000004

DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19

DwmSetWindowAttribute = dwmapi.DwmSetWindowAttribute
DwmSetWindowAttribute.argtypes = [wintypes.HWND, wintypes.DWORD, wintypes.LPCVOID, wintypes.DWORD]
DwmSetWindowAttribute.restype = HRESULT

class MARGINS(Structure):
    _fields_ = [
        ('cxLeftWidth', c_int),
        ('cxRightWidth', c_int),
        ('cyTopHeight', c_int),
        ('cyBottomHeight', c_int)
    ]

class DWM_BLURBEHIND(Structure):
    _fields_ = [
        ('dwFlags', wintypes.DWORD),
        ('fEnable', wintypes.BOOL),
        ('hRgnBlur', wintypes.HRGN),
        ('fTransitionOnMaximized', wintypes.BOOL)
    ]

class LUID(Structure):
    _fields_ = [
        ('LowPart', wintypes.DWORD),
        ('HighPart', wintypes.LONG),
    ]

class LUID_AND_ATTRIBUTES(Structure):
    _fields_ = [
        ('Luid', LUID),
        ('Attributes', wintypes.DWORD),
    ]

class TOKEN_PRIVILEGES(Structure):
    _fields_ = [
        ('PrivilegeCount', wintypes.DWORD),
        ('Privileges', LUID_AND_ATTRIBUTES * 1),
    ]

def enable_shutdown_privilege():
    h_token = wintypes.HANDLE()
    if not windll.advapi32.OpenProcessToken(
        windll.kernel32.GetCurrentProcess(),
        TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY,
        byref(h_token)
    ):
        return False

    try:
        tkp = TOKEN_PRIVILEGES()

        if not windll.advapi32.LookupPrivilegeValueW(
            None,
            'SeShutdownPrivilege',
            byref(tkp.Privileges[0].Luid)
        ):
            return False

        tkp.PrivilegeCount = 1
        tkp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED

        result = windll.advapi32.AdjustTokenPrivileges(
            h_token,
            False,
            byref(tkp),
            0,
            None,
            None
        )

        last_error = windll.kernel32.GetLastError()
        return bool(result) and last_error == ERROR_SUCCESS
    finally:
        kernel32.CloseHandle(h_token)

def schedule_shutdown(delay_seconds, message='', reboot=False, force=False):
    if not enable_shutdown_privilege():
        raise RuntimeError('Failed to enable shutdown privilege')

    message_ptr = None
    if message:
        message_ptr = c_wchar_p(message)

    reason = (SHTDN_REASON_MAJOR_APPLICATION |
              SHTDN_REASON_MINOR_INSTALLATION |
              SHTDN_REASON_FLAG_PLANNED)

    result = windll.advapi32.InitiateSystemShutdownExW(
        None,                    # lpMachineName (local machine)
        message_ptr,             # lpMessage
        delay_seconds,           # dwTimeout
        force,                   # bForceAppsClosed
        reboot,                  # bRebootAfterShutdown
        reason                   # dwReason
    )

    if not result:
        error = kernel32.GetLastError()
        raise RuntimeError(f'InitiateSystemShutdownExW failed with error: {error}')

    return True

def abort_shutdown():
    if not enable_shutdown_privilege():
        raise RuntimeError('Failed to enable shutdown privilege')

    result = advapi32.AbortSystemShutdownW(None)

    if not result:
        error = kernel32.GetLastError()
        raise RuntimeError(f'AbortSystemShutdownW failed with error: {error}')

    return True

def log_out():
    user32.ExitWindowsEx(0, 0)

def lock():
    user32.LockWorkStation()

def is_dark_mode():
    try:
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        key = OpenKey(registry, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        value, _ = QueryValueEx(key, 'AppsUseLightTheme')
        CloseKey(key)
        return value == 0
    except:
        return False

def use_immersive_dark_mode(window: QWidget):
    if is_dark_mode() and QApplication.style().name() != 'Fusion':
        hwnd = window.winId()
        value = c_bool(True)
        result = DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, byref(value), 4)
        if result != 0:
            DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1, byref(value), 4)
