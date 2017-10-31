from sense_hat import SenseHat # it is sense_emu when using pi emulator
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
br = (244,164,96) # Brown
g = (0,104,10) # green
y = (253,184,19) # yellow
b = (0,191,255) # blue
color_two = (255,0,0) # idk this color
l = (0,0,0) # blank

# Functions ---------------------------
tom_pixels = [
    l, l, l, l, l, l, l, l,
    l, l, l, l, l, br, l, l,
    l, l, l, l, l, br, br, l,
    l, l, br, br, br, br, l, l,
    l, br, br, br, br, br, l, l,
    l, l, br, l, l, br, l, l,
    l, l, br, l, l, br, l, l,
    l, l, l, l, l, l, l, l,
    ]

tom_pixels_with_setting = [
    y, y, b, b, b, b, b, b,
    y, y, b, b, b, br, b, b,
    b, b, b, b, b, br, br, b,
    b, b, br, br, br, br, b, b,
    b, br, br, br, br, br, b, b,
    b, b, br, b, b, br, b, b,
    b, b, br, b, b, br, b, b,
    g, g, g, g, g, g, g, g,
    ]

# Main program ------------------------
sense.clear()
sense.set_pixels(tom_pixels_with_setting)
