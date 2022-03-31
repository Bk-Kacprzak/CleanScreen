from AppKit import NSWorkspace
import ApplicationServices as AppServ
import Quartz 
from application_window import ApplicationRect
from Foundation import NSNotificationCenter
import MASShortcut as MassShortcut

class ActiveWindow() :
    def __init__(self) :
        self.app_name = str()
        self.app_pid = int()
        self.active_screen_index = int()
        self.window_size = ApplicationRect(0, 0, 0, 0)
        self.app_ref = None

    def get_frontmost_application(self) : 
        frontmost_application =  NSWorkspace.sharedWorkspace().activeApplication()
        self.app_ref = AppServ.AXUIElementCreateApplication(frontmost_application["NSApplicationProcessIdentifier"])
        
    def get_application_info(self) :
        app_info =  NSWorkspace.sharedWorkspace().activeApplication()
        self.app_name = app_info["NSApplicationName"]
        self.app_pid = app_info["NSApplicationProcessIdentifier"]

    def get_application_size(self, window) :
        app_rect = self.get_window_size()
        self.active_screen_index = app_rect.set_window_location()
        self.window_size = window(self.active_screen_index)

    def set_position(self, UAXUIElement) :
        new_coordinates = AppServ.CGPoint(self.window_size.x, self.window_size.y)
        position = AppServ.AXValueCreate(AppServ.kAXValueCGPointType, new_coordinates)
        AppServ.AXUIElementSetAttributeValue(UAXUIElement, AppServ.kAXPositionAttribute, position)

    def set_window_size(self, UAXUIElement) :
        new_size = AppServ.CGSize(self.window_size.width,self.window_size.height)
        size = AppServ.AXValueCreate(AppServ.kAXValueCGSizeType, new_size)
        AppServ.AXUIElementSetAttributeValue(UAXUIElement, AppServ.kAXSizeAttribute, size)
        AppServ.AXUIElementSetAttributeValue(UAXUIElement, AppServ.kAXSizeAttribute, size)

    def get_window_size(self) :
        windows = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListExcludeDesktopElements | Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
        window_info = None
        for win in windows:
            if self.app_name in (win[Quartz.kCGWindowOwnerName], win.get(Quartz.kCGWindowName, '')):
                window_info = win["kCGWindowBounds"]
                break
        return ApplicationRect(window_info["X"], window_info["Y"], window_info["Width"], window_info["Height"])

    def resize(self, window : ApplicationRect.count_window_size) :
        self.get_frontmost_application()
        self.get_application_info()
        self.get_application_size(window)
        app_windows = AppServ.AXUIElementCreateApplication(self.app_pid) #AXUIElementRef
        # get list of windows with the same PID ""
        window_list = AppServ.AXUIElementCopyAttributeValue(self.app_ref, AppServ.kAXWindowsAttribute, None)

        # get front app window from the list
        AXUIElement = window_list[1][0] #AXUIElement

        AppServ.AXUIElementSetAttributeValue(self.app_ref, "AXEnhancedUserInterface", False)

        self.set_position(AXUIElement)
        self.set_window_size(AXUIElement)

        AppServ.AXUIElementSetAttributeValue(self.app_ref, "AXEnhancedUserInterface", True)

    # def test(self):
    #     NSNotificationCenter.defaultCenter().removeObserver_(self)
    #
    #
    #     combination = dict()
    #     for shortcut in shortcuts:
    #         MassShortcut.MASShortcutBinder.sharedBinder().breakBindingWithDefaultsKey_(shortcut.id)
    #         combination[shortcut.id] = shortcut.combination
    #
    #     MassShortcut.MASShortcutBinder.sharedBinder().registerDefaultShortcuts_(combination)


        

        

                    
application = ActiveWindow()
