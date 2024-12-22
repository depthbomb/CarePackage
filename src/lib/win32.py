from ctypes import windll

_user32 = windll.user32

def log_out():
    _user32.ExitWindowsEx(0, 0)

def lock():
    _user32.LockWorkStation()
