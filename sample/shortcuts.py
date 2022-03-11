from application_window import ApplicationWindow
from screen import Screen

_CMD = "Key.cmd"
_OPTION = "Key.alt"
_CTRL = "Key.ctrl"
_SHIFT = "Key.shift"
_CMD_RIGHT = "Key.cmd_r"
_OPTION_RIGHT = "Key.alt_r"
_SHIFT_RIGHT = "Key.shift_r"

_UP = "Key.up"
_DOWN = "Key.down"
_RIGHT = "Key.right"
_LEFT = "Key.left"

class Shortcut : 
    def __init__(self, combination, window) : 
        self.combination = combination
        self.window = window
        
window = ApplicationWindow.count_window_size

shortcuts = [
    Shortcut({_CTRL, _OPTION, _RIGHT}, window(Screen.RIGHT_HALF_POSITION, 0, Screen.HALF_SCREEN_SIZE, Screen.FULL_SCREEN_SIZE)),

    Shortcut({_CTRL, _OPTION, _LEFT}, window(Screen.ORIGIN_POSITION, 0, Screen.HALF_SCREEN_SIZE, Screen.FULL_SCREEN_SIZE)),

    Shortcut({_CMD, _OPTION, _LEFT}, window(Screen.ORIGIN_POSITION, 0, Screen.ONE_THIRD_SCREEN_SIZE, Screen.FULL_SCREEN_SIZE)),

    Shortcut({_CMD, _OPTION, _RIGHT}, window(Screen.RIGHT_ONE_THIRD_POSITION, 0, Screen.ONE_THIRD_SCREEN_SIZE, Screen.FULL_SCREEN_SIZE)),
    Shortcut({_CMD, _OPTION, _UP}, window(Screen.CENTER_ONE_THIRD_POSITION, 0, Screen.ONE_THIRD_SCREEN_SIZE, Screen.FULL_SCREEN_SIZE)),
    ]
