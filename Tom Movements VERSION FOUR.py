from sense_hat import *
from random import randint

sense = SenseHat()
sense.clear()
temp = sense.get_temperature()
event = sense.stick

import time

# Variables ---------------------------
br = (244,164,96)  #Color: Brown
g  = (0,104,10)    #Color: Green
y  = (253,184,19)  #Color: Yellow
b  = (0,191,255)   #Color: Blue
gr = (192,192,192) #Color: Gray
o  = (255,20,60)   #Color: Red
l  = (0,0,0)       #Color: Blank
game_over = False  #Game Status: Running (default)
tamagatchi = True

tom_pixels_logo = [
    l, l, l, l, l, l, l, l,
    l, l, l, l, l, br, l, l,
    l, l, l, l, l, br, br, l,
    l, l, br, br, br, br, l, l,
    l, br, br, br, br, br, l, l,
    l, l, br, l, l, br, l, l,
    l, l, br, l, l, br, l, l,
    l, l, l, l, l, l, l, l,
    ]

# Functions ------------------------------------------------

def set_scene():
    if temp > 30.4:  # Sun changes b/c of temp to be: RED
      tom_pixels_right_1 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, br, l, l,
        l, l, l, l, l, br, br, l,
        l, l, br, br, br, br, l, l,
        l, br, br, br, br, br, l, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_2 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, l, br, l,
        l, l, l, l, l, l, br, br,
        l, l, l, br, br, br, br, l,
        l, l, br, br, br, br, br, l,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_3 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, l, l, br,
        br, l, l, l, l, l, l, br,
        l, l, l, l, br, br, br, br,
        l, l, l, br, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_4 = [
        o, o, l, l, l, l, l, l,
        br, o, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        br, l, l, l, l, br, br, br,
        br, l, l, l, br, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_5 = [
        o, o, l, l, l, l, l, l,
        o, br, l, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        br, br, l, l, l, l, br, br,
        br, br, l, l, l, br, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_6 = [
        o, o, l, l, l, l, l, l,
        o, o, br, l, l, l, l, l,
        l, l, br, br, l, l, l, l,
        br, br, br, l, l, l, l, br,
        br, br, br, l, l, l, br, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_7 = [
        o, o, l, l, l, l, l, l,
        o, o, l, br, l, l, l, l,
        l, l, l, br, br, l, l, l,
        br, br, br, br, l, l, l, l,
        br, br, br, br, l, l, l, br,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_8 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, br, l, l, l,
        l, l, l, l, br, br, l, l,
        l, br, br, br, br, l, l, l,
        br, br, br, br, br, l, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l,br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_1 = [
        o, o, l, l, l, l, l, l,
        o, o, br, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        l, l, br, br, br, br, l, l,
        l, l, br, br, br, br, br, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_2 = [
        o, o, l, l, l, l, l, l,
        o, br, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        l, br, br, br, br, l, l, l,
        l, br, br, br, br, br, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l, br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_3 = [
        o, o, l, l, l, l, l, l,
        br, o, l, l, l, l, l, l,
        br, l, l, l, l, l, l, br,
        br, br, br, br, l, l, l, l,
        br, br, br, br, br, l, l, l,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_4 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, l, l, br,
        l, l, l, l, l, l, br, br,
        br, br, br, l, l, l, l, br,
        br, br, br, br, l, l, l, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_5 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, l, br, l,
        l, l, l, l, l, br, br, l,
        br, br, l, l, l, l, br, br,
        br, br, br, l, l, l, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_6 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, l, br, l, l,
        l, l, l, l, br, br, l, l,
        br, l, l, l, l, br, br, br,
        br, br, l, l, l, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_7 = [
        o, o, l, l, l, l, l, l,
        o, o, l, l, br, l, l, l,
        l, l, l, br, br, l, l, l,
        l, l, l, l, br, br, br, br,
        br, l, l, l, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_8 = [
        o, o, l, l, l, l, l, l,
        o, o, l, br, l, l, l, l,
        l, l, br, br, l, l, l, l,
        l, l, l, br, br, br, br, l,
        l, l, l, br, br, br, br, br,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
    elif temp >= 29.5 and temp <= 30.4: # Sun is set at default: YELLOW
      tom_pixels_right_1 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, br, l, l,
        l, l, l, l, l, br, br, l,
        l, l, br, br, br, br, l, l,
        l, br, br, br, br, br, l, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_2 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, l, br, l,
        l, l, l, l, l, l, br, br,
        l, l, l, br, br, br, br, l,
        l, l, br, br, br, br, br, l,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_3 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, l, l, br,
        br, l, l, l, l, l, l, br,
        l, l, l, l, br, br, br, br,
        l, l, l, br, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_4 = [
        y, y, l, l, l, l, l, l,
        br, y, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        br, l, l, l, l, br, br, br,
        br, l, l, l, br, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_5 = [
        y, y, l, l, l, l, l, l,
        y, br, l, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        br, br, l, l, l, l, br, br,
        br, br, l, l, l, br, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_6 = [
        y, y, l, l, l, l, l, l,
        y, y, br, l, l, l, l, l,
        l, l, br, br, l, l, l, l,
        br, br, br, l, l, l, l, br,
        br, br, br, l, l, l, br, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_7 = [
        y, y, l, l, l, l, l, l,
        y, y, l, br, l, l, l, l,
        l, l, l, br, br, l, l, l,
        br, br, br, br, l, l, l, l,
        br, br, br, br, l, l, l, br,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_8 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, br, l, l, l,
        l, l, l, l, br, br, l, l,
        l, br, br, br, br, l, l, l,
        br, br, br, br, br, l, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l,br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_1 = [
        y, y, l, l, l, l, l, l,
        y, y, br, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        l, l, br, br, br, br, l, l,
        l, l, br, br, br, br, br, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_2 = [
        y, y, l, l, l, l, l, l,
        y, br, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        l, br, br, br, br, l, l, l,
        l, br, br, br, br, br, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l, br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_3 = [
        y, y, l, l, l, l, l, l,
        br, y, l, l, l, l, l, l,
        br, l, l, l, l, l, l, br,
        br, br, br, br, l, l, l, l,
        br, br, br, br, br, l, l, l,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_4 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, l, l, br,
        l, l, l, l, l, l, br, br,
        br, br, br, l, l, l, l, br,
        br, br, br, br, l, l, l, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_5 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, l, br, l,
        l, l, l, l, l, br, br, l,
        br, br, l, l, l, l, br, br,
        br, br, br, l, l, l, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_6 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, l, br, l, l,
        l, l, l, l, br, br, l, l,
        br, l, l, l, l, br, br, br,
        br, br, l, l, l, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_7 = [
        y, y, l, l, l, l, l, l,
        y, y, l, l, br, l, l, l,
        l, l, l, br, br, l, l, l,
        l, l, l, l, br, br, br, br,
        br, l, l, l, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_8 = [
        y, y, l, l, l, l, l, l,
        y, y, l, br, l, l, l, l,
        l, l, br, br, l, l, l, l,
        l, l, l, br, br, br, br, l,
        l, l, l, br, br, br, br, br,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      
    elif temp < 29.5: # Sun changes b/c of temp to be: GRAY
      tom_pixels_right_1 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, br, l, l,
        l, l, l, l, l, br, br, l,
        l, l, br, br, br, br, l, l,
        l, br, br, br, br, br, l, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_2 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, l, br, l,
        l, l, l, l, l, l, br, br,
        l, l, l, br, br, br, br, l,
        l, l, br, br, br, br, br, l,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_3 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, l, l, br,
        br, l, l, l, l, l, l, br,
        l, l, l, l, br, br, br, br,
        l, l, l, br, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_4 = [
        gr, gr, l, l, l, l, l, l,
        br, gr, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        br, l, l, l, l, br, br, br,
        br, l, l, l, br, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_5 = [
        gr, gr, l, l, l, l, l, l,
        gr, br, l, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        br, br, l, l, l, l, br, br,
        br, br, l, l, l, br, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_6 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, br, l, l, l, l, l,
        l, l, br, br, l, l, l, l,
        br, br, br, l, l, l, l, br,
        br, br, br, l, l, l, br, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_7 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, br, l, l, l, l,
        l, l, l, br, br, l, l, l,
        br, br, br, br, l, l, l, l,
        br, br, br, br, l, l, l, br,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_right_8 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, br, l, l, l,
        l, l, l, l, br, br, l, l,
        l, br, br, br, br, l, l, l,
        br, br, br, br, br, l, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l,br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_1 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, br, l, l, l, l, l,
        l, br, br, l, l, l, l, l,
        l, l, br, br, br, br, l, l,
        l, l, br, br, br, br, br, l,
        l, l, br, l, l, br, l, l,
        l, l, br, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_2 = [
        gr, gr, l, l, l, l, l, l,
        gr, br, l, l, l, l, l, l,
        br, br, l, l, l, l, l, l,
        l, br, br, br, br, l, l, l,
        l, br, br, br, br, br, l, l,
        l, br, l, l, br, l, l, l,
        l, br, l, l, br, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_3 = [
        gr, gr, l, l, l, l, l, l,
        br, gr, l, l, l, l, l, l,
        br, l, l, l, l, l, l, br,
        br, br, br, br, l, l, l, l,
        br, br, br, br, br, l, l, l,
        br, l, l, br, l, l, l, l,
        br, l, l, br, l, l, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_4 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, l, l, br,
        l, l, l, l, l, l, br, br,
        br, br, br, l, l, l, l, br,
        br, br, br, br, l, l, l, br,
        l, l, br, l, l, l, l, br,
        l, l, br, l, l, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_5 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, l, br, l,
        l, l, l, l, l, br, br, l,
        br, br, l, l, l, l, br, br,
        br, br, br, l, l, l, br, br,
        l, br, l, l, l, l, br, l,
        l, br, l, l, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_6 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, l, br, l, l,
        l, l, l, l, br, br, l, l,
        br, l, l, l, l, br, br, br,
        br, br, l, l, l, br, br, br,
        br, l, l, l, l, br, l, l,
        br, l, l, l, l, br, l, l,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_7 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, l, br, l, l, l,
        l, l, l, br, br, l, l, l,
        l, l, l, l, br, br, br, br,
        br, l, l, l, br, br, br, br,
        l, l, l, l, br, l, l, br,
        l, l, l, l, br, l, l, br,
        g, g, g, g, g, g, g, g,
        ]
      tom_pixels_left_8 = [
        gr, gr, l, l, l, l, l, l,
        gr, gr, l, br, l, l, l, l,
        l, l, br, br, l, l, l, l,
        l, l, l, br, br, br, br, l,
        l, l, l, br, br, br, br, br,
        l, l, l, br, l, l, br, l,
        l, l, l, br, l, l, br, l,
        g, g, g, g, g, g, g, g,
        ]
        
    if pitch <= 1:
          sense.set_pixels(tom_pixels_logo)
          time.sleep(0.2)
    if 359 > pitch > 179:
          sense.set_pixels(tom_pixels_right_1)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_2)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_3)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_4)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_5)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_6)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_7)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_right_8)
          time.sleep(0.2)
    elif 1 < pitch < 179:
          sense.set_pixels(tom_pixels_left_1)
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_2)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_3)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_4)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_5)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_6)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_7)          
          time.sleep(0.2)
          sense.set_pixels(tom_pixels_left_8)          
          time.sleep(0.2)

def end_game():
  #game_over = True
  sense.show_message("Game Over")

## Main ----------------------------------------------------------
while tamagatchi:
  while game_over == False:
    event = sense.stick
  
    for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'up':
            game_over = True
            end_game()
        if event.action == 'pressed' and event.direction == 'down':
            game_over = True
            end_game()
        if event.action == 'pressed' and event.direction == 'right':
            game_over = True
            end_game()
        if event.action == 'pressed' and event.direction == 'left':
            game_over = True
            end_game()
    print(temp)
    temp = sense.get_temperature()
    pitch = sense.get_orientation()['pitch'] ##Obtains the gyroscope readings
    set_scene()
    time.sleep(0.1)
  while game_over == True:
      event = sense.stick

      sense.set_pixels(tom_pixels_logo)
      for event in sense.stick.get_events():
        if event.action == 'pressed' and event.direction == 'middle':
          game_over = False
        if event.action == 'pressed' and event.direction == 'up':
          game_over = False
        if event.action == 'pressed' and event.direction == 'down':
          game_over = False
        if event.action == 'pressed' and event.direction == 'right':
          game_over = False
        if event.action == 'pressed' and event.direction == 'left':
          game_over = False
