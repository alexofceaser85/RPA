#!/usr/bin/env python3

import pyautogui

__author__ = "Alexander Ayers"
__version__ = "Southwire Hackathon"


def open_eclipse():
    eclipse_taskbar_location = pyautogui.locateOnScreen("images/Eclipse.png", confidence=.7)
    pyautogui.moveTo(eclipse_taskbar_location[0] + 15, eclipse_taskbar_location[1] + 5)
    pyautogui.click()

def load_files(file_location):
    is_eclipse_open = False
    while not is_eclipse_open:
        if (pyautogui.locateOnScreen("images/File_Menu_Text.png") != None):
            is_eclipse_open = True
    print("reached")
    pyautogui.press("alt")
    pyautogui.press("f")
    for x in range(15):
        pyautogui.press("down")
    pyautogui.click()
    
def main():
    open_eclipse() 
    load_files("")

if __name__ == "__main__":
    main()