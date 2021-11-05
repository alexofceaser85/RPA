#!/usr/bin/env python3

import pyautogui

__author__ = "Alexander Ayers"
__version__ = "Southwire Hackathon"


pyautogui.press('win')
pyautogui.typewrite("eclipse")
pyautogui.press("enter")

def main():
    print("Hello World")

if __name__ == "__main__":
    main()