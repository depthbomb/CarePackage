from enum import auto, IntEnum

class PostOperationAction(IntEnum):
    DoNothing = auto()
    CloseApp = auto()
    LogOut = auto()
    Lock = auto()
    Restart = auto()
    ShutDown = auto()
