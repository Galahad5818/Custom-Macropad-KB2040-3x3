import usb_hid
import os
import board
import neopixel
import time
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_fr import KeyboardLayout
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Initialisation des périphériques HID
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)
cc = ConsumerControl(usb_hid.devices)

# Gestion de la LED intégrée
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.3

def set_led(map_id):
    """Change la couleur de la LED selon la map active"""
    if map_id == 1:
        pixel.fill((255, 0, 0))  # Rouge pour Map 1
    else:
        pixel.fill((0, 0, 255))  # Bleu pour Map 2

# Fonctions personnalisées pour des actions complexes

def Start_Programme(CheminPara):
    keyboard.press(Keycode.WINDOWS, Keycode.R)
    keyboard.release(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.2)
    layout.write(CheminPara)

def Deverouillage():
    keyboard.press(Keycode.SPACE)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.5)
    layout.write("CODE VERROUILLAGE DU PC\n")

def Verouillage():
    keyboard.press(Keycode.WINDOWS, Keycode.L)
    keyboard.release(Keycode.WINDOWS, Keycode.L)

def Eteindre_PC():
    Start_Programme("shutdown -p\n")






###
### Map 1
###
def map1_actions(key):
    actions = {
        #0 changement de map
        1: lambda: Deverouillage(),
        2: lambda: layout.write("12\n"),
        3: lambda: Start_Programme("C:\\Users\\NOM DE VOTRE PC\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe\n"),
        4: lambda: Start_Programme('chrome.exe --profile-directory="Default" https://www.youtube.com\n'),
        5: lambda: Start_Programme("C:\\Users\\NOM DE VOTRE PC\\AppData\\Roaming\\Spotify\\Spotify.exe\n"),
        6: lambda: Start_Programme("shutdown -h\n"), #Veille prolonger
        7: lambda: Verouillage(),
        8: lambda: layout.write("12\n"),
    }
    if key in actions:
        actions[key]()


###
### Map 2
###
def map2_actions(key):
    actions = {
        1: lambda: type_numbers("565565"),
    }
    if key in actions:
        actions[key]()


