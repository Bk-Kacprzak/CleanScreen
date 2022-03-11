from AppKit import NSScreen, NSPoint, NSEvent, NSRect
import Foundation

class Screen: 
    TOTAL_SCREENS_WIDTH = 0
    ORIGIN_POSITION = 0 

    # 1/4 split
    LEFT_QUARTER_POSITION = 1/4
    RIGHT_QUARTER_POSITION = 2/4
    MOST_RIGTH_QUARTER_POSITION = 3/4
    
    # 1/3 split
    CENTER_ONE_THIRD_POSITION = 1/3
    RIGHT_ONE_THIRD_POSITION = 2/3 

    # 1/2 split
    RIGHT_HALF_POSITION = 1/2
    
    # size 
    HALF_SCREEN_SIZE = 1/2 
    ONE_THIRD_SCREEN_SIZE = 1/3 
    QUATER_SCREEN_SIZE = 1/4 
    FULL_SCREEN_SIZE = 1

    def __init__(self, width, height, screen_id, origin_x, origin_y)  :
        self.size = (width, height)
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.screen_id = screen_id
        Screen.TOTAL_SCREENS_WIDTH += width
        
    @staticmethod
    def get_active_screen() : 
        #todo: refactor it by using Listener to get cooridnates of last mouseclick 

        mouse_location = NSEvent.mouseLocation()
        screen_enumerator = NSScreen.screens().objectEnumerator()
        screen = screen_enumerator.nextObject()

        if not Foundation.NSMouseInRect(mouse_location, screen.frame(), Foundation.NO): 
            screen = screen_enumerator.nextObject()

        return screen 

    # TODO: translate operation system coordinates to coordinates where (0,0) is far left screen
    @staticmethod 
    def redefine_global_coordinates(screens) : 
        if len(screens) == 1 : 
            return 

        # far left window
        screens.sort(key = lambda screen: screen.origin_x, reverse = False)
        for i in range(len(screens) - 1, -1, -1):
            screens[i].origin_x += abs(screens[0].origin_x)
   
    @staticmethod 
    def get_top_left_screen(screens) : 
        x_coordinates = []
        for screen in screens: 
            x_coordinates.append(screen.origin_x) 
        
        return screens[x_coordinates.index(min(x_coordinates))]

    # TODO: create method that translate coordinate system in application to operation system coordinates

screens = [] 
for screen in NSScreen.screens():
    screens.append(Screen(*screen.visibleFrame().size, screen.deviceDescription()["NSScreenNumber"],screen.frame().origin.x, screen.frame().origin.y))

for screen in screens  : 
    print(screen.__dict__)