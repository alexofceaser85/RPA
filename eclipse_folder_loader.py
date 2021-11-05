#!/usr/bin/env python3

import pyautogui

__author__ = "Alexander Ayers"
__version__ = "Southwire Hackathon"


def open_eclipse():
    pyautogui.press('win')
    pyautogui.typewrite("eclipse")
    pyautogui.press("enter")

def load_files(file_location):
    return ""
    
def main():
    print("Hello World")    

if __name__ == "__main__":
    main()