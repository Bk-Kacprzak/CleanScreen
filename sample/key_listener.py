from pynput.keyboard import Key, Listener
from shortcuts import shortcuts
from active_window import application

class KeyListener :
    KEY_COMBINATION = set()

    def __init__(self) : 
        self.listener = Listener(self.on_press, self.on_release) 
        self.listener.start()
        self.listener.join()
    @staticmethod
    def on_press(key) -> bool :
        if not isinstance(key, Key) : 
            return
        key_string = str(key)
        KeyListener.KEY_COMBINATION.add(key_string)
        print(KeyListener.KEY_COMBINATION)
 
        "Check if specific combination exist"
        # WARNING : issubset is used to prevent from unremoved cmd_r / ctrl_r from the key_combination
        for shortcut in shortcuts: 
            if shortcut.combination.issubset(KeyListener.KEY_COMBINATION) :
                application.resize(shortcut.window) 

            
    @staticmethod 
    def on_release(key) : 
        key_string = str(key)
        try:
            KeyListener.KEY_COMBINATION.remove(key_string)
        except KeyError:
            print(f"{key_string} is not an item in KeyListener.KEY_COMBINATION")


listener = KeyListener()
