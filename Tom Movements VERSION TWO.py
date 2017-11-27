from sense_hat import *
from random import randint

sense = SenseHat()
sense.clear()
temp = sense.get_temperature()

import time

# Variables ---------------------------
br = (244,164,96)  #Color: Brown
g  = (0,104,10)    #Color: Green
y  = (253,184,19)  #Color: Yellow
b  = (0,191,255)   #Color: Blue
gr = (192,192,192) #Color: Gray
o  = (255,140,0)   #Color: Orange
l  = (0,0,0)       #Color: Blank

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

if temp > 29.7:  # Sun changes b/c of temp to be: ORANGE
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
elif temp >= 29.0 and temp <= 29.7: # Sun is set at default: YELLOW
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
  
elif temp < 29.0: # Sun changes b/c of temp to be: GRAY
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
    
game_over = False
   
# Functions ------------------------------------------------
'''main move function to play the animation'''
def move_place():
      if pitch == 0:
          sense.set_pixels(tom_pixels_with_setting)
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
          
## Main ----------------------------------------------------------


while game_over == False:
  pitch = sense.get_orientation()['pitch'] ##Obtains the gyroscope readings
  move_place()
  time.sleep(0.1)
