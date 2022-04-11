from screen import screens, Screen
from action_manager import WindowDimensionsRatio

class ApplicationRect:

    def __init__ (self, x, y, w, h) :
        # application window coordinates
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.window_location = self.set_window_location() 

    def set_window_location(self) :
        "returns index of screen"   
        if(len(screens) == 1) :
            return 0 
        
        top_left_screen = Screen.get_top_left_screen(screens)

        for screen in screens: 
            if screen.origin_x <= self.x < screen.origin_x + screen.width: 
                return screens.index(screen)
            
            if self.x < top_left_screen.origin_x : 
                return screens.index(top_left_screen)

    @staticmethod 
    def count_window_size(windowDimension : WindowDimensionsRatio) : 
        def count_size(screen_index) : 
            # TODO: refactor function using another coordinate system written before in ./screen.py
            if windowDimension.x_ratio == 0 :
                x = screens[screen_index].origin_x
            else:
                if screens[screen_index].origin_x + screens[screen_index].width == 0 : 
                    "this is first left screen next to main screen"
                    x = screens[screen_index].origin_x
                    x *= (1-windowDimension.x_ratio)
                else : 
                    x = screens[screen_index].origin_x + screens[screen_index].width * windowDimension.x_ratio

            y = screens[screen_index].origin_y + screens[screen_index].height
            y *= windowDimension.y_ratio

            width = screens[screen_index].width * windowDimension.w_ratio
            height = screens[screen_index].height * windowDimension.h_ratio

            return ApplicationRect(x, y, width, height)

        
        return count_size

# INFO
# visibleFrame() is more important than frame() to set specific width/height 
# IMPORTANT 
# Main Screen has (0,0) coordinates on the top left point 
# If another screen is on the left side - x coordinates are negative, otherwise x coords are positive 
# Before any calculation - get visibleFrame of each screen and calculate TOTAL WIDTH



