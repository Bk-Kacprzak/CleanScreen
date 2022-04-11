from enum import Enum

class WindowAction(Enum): 
    HALF_LEFT = 0
    HALF_RIGHT = 1
    LEFT_THIRD = 20
    MIDDLE_THIRD = 22
    RIGHT_THIRD = 24 
    FIRST_FOURTH = 31
    SECOND_FOURTH = 32
    THIRD_FOURTH = 33
    LAST_FOURTH = 34

actions = [
    WindowAction.HALF_LEFT,
    WindowAction.HALF_RIGHT,
    WindowAction.LEFT_THIRD,
    WindowAction.MIDDLE_THIRD,
    WindowAction.RIGHT_THIRD,
    WindowAction.FIRST_FOURTH,
    WindowAction.SECOND_FOURTH,
    WindowAction.THIRD_FOURTH,
    WindowAction.LAST_FOURTH
]