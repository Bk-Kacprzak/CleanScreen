from application_window import ApplicationRect
from screen import Screen
from action_manager import actionManager, WindowAction

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
    def __init__(self, action, combination) :
        self.action = action
        self.combination = combination
        self.window = window(actionManager[action])

window = ApplicationRect.count_window_size

shortcuts = [
  
    Shortcut(
        WindowAction.HALF_LEFT,
        {_CTRL, _OPTION, _LEFT}
    ),
    Shortcut(
        WindowAction.HALF_RIGHT,
        {_CTRL, _OPTION, _RIGHT}
    ),
    Shortcut(
        WindowAction.LEFT_THIRD,
        {_CMD, _OPTION, _LEFT}
    ),
    
      Shortcut(
        WindowAction.MIDDLE_THIRD,
        {_CMD, _OPTION, _UP}
    ),
    Shortcut(
        WindowAction.RIGHT_THIRD,
        {_CMD, _OPTION, _RIGHT}
    ),
    Shortcut( 
        WindowAction.FIRST_FOURTH,
        {_CTRL,_SHIFT,_LEFT}
    ),
    Shortcut( 
        WindowAction.SECOND_FOURTH,
        {_CTRL,_SHIFT,_UP}
    ),
    Shortcut( 
        WindowAction.THIRD_FOURTH,
        {_CTRL,_SHIFT,_DOWN}
    ),
    Shortcut( 
        WindowAction.LAST_FOURTH,
        {_CTRL,_SHIFT,_RIGHT}
    )
]