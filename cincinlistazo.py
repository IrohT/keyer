import keyboard
import os
import datetime
from pynput.mouse import Listener

def record_mouse_events():
    
    def on_click(x, y, button, pressed):
            if pressed:
                ido = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{ido} - {button} clicked at ({x}, {y})\n")

    def on_scroll(x, y, dx, dy):
        ido = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{ido} - mouse scrolled at ({x}, {y})\n")
               
    with open(".\eger.txt", "a") as f:
         with Listener(on_click=on_click, on_scroll=on_scroll) as listener:
            key = keyboard.read_key()
            if key == 'esc':    
                listener.stop()

record_mouse_events()
