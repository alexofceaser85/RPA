#!/usr/bin/env python3

import pyautogui
import os
from PIL import Image, ImageDraw, ImageFont

__author__ = "Alexander Ayers"
__version__ = "Southwire Hackathon"

vm_arguments = '--module-path "${eclipse_home}/javafx-sdk-14.0.2.1/lib" --add-modules javafx.controls,javafx.fxml'

def open_eclipse():
    eclipse_taskbar_location = pyautogui.locateOnScreen("images/Eclipse.png", confidence=.7)
    pyautogui.moveTo(eclipse_taskbar_location[0] + 15, eclipse_taskbar_location[1] + 5)
    pyautogui.click()

def move_to_file_menu():
    file_menu_location = None
    while file_menu_location == None:
        file_menu_location = pyautogui.locateOnScreen("images/File_Menu_Text.png", confidence=.8)
    pyautogui.press("alt")
    pyautogui.press("f")
    for x in range(15):
        pyautogui.press("down")
    pyautogui.press("enter")
    pyautogui.press("down")
    for x in range(3):
        pyautogui.press("up")
    for x in range(2):
        pyautogui.press("down")
    pyautogui.press("enter")
    

def load_files(file_location: str):
    zip_files = os.listdir(file_location)
    for file in zip_files:
      print(os.getcwd() + "\\" + file_location + "\\" + file)
      
    
def main():
    open_eclipse()
    move_to_file_menu()
    file_location = "files"
    file = "CS3152Lab1AlexanderAyers.zip"
    load_files(file_location, file)

def load_files(file_location, file):
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.click()
    pyautogui.typewrite(os.getcwd() + "\\" + file_location + "\\" + file)
    browse_location = pyautogui.locateOnScreen("images/Browse.png")
    pyautogui.moveTo(browse_location[0] + 50, browse_location[1] + 10)
    pyautogui.click()
    for x in range(11):
     pyautogui.press("tab")
    pyautogui.press("enter")
    # temp_image = Image.new('RGB', (500, 50), color=(47,47,47))
    # font = ImageFont.truetype('Arial.ttf', size=10)
    # canvas = ImageDraw.Draw(temp_image)
    # canvas.text((10, 10), file,font=font, fill="#6d858f")
    # pyautogui.moveTo(50, 120)
    # pyautogui.rightClick()
    
    

if __name__ == "__main__":
    main()