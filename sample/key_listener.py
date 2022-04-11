from pynput.keyboard import Key, Listener
from shortcuts import shortcuts
from active_window import application

class KeyListener(Listener) :
    "Class responsible for hotkey listening"
    KEY_COMBINATION = set()
    def __init__(self) : 
        super().__init__(
            on_press = self.on_press,
            on_release=  self.on_release,
            suppress = False)

        self.start()
        self.join()

    def on_press(self,key) -> bool :
        if not isinstance(key, Key) : 
            return
        key_string = str(key)

        KeyListener.KEY_COMBINATION.add(key_string)
        # Check if specific combination exist
       
        # WARNING : issubset is used to prevent from unremoved cmd_r / ctrl_r from the key_combination
        for shortcut in shortcuts: 
            if shortcut.combination.issubset(KeyListener.KEY_COMBINATION) :
                application.resize(shortcut.window) 


    def on_release(self,key) : 
        key_string = str(key)
        try:
            KeyListener.KEY_COMBINATION.remove(key_string)
        except KeyError:
            print(f"{key_string} is not an item in KeyListener.KEY_COMBINATION")


listener = KeyListener()
