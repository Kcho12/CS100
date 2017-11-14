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
variable = True

# Functions ---------------------------
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

def draw_tom_right():
  sense.set_pixels(tom_pixels_right_1)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_2)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_3)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_4)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_5)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_6)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_7)
  sleep(.15)
  sense.set_pixels(tom_pixels_right_8)
  sleep(.15)
  
def draw_tom_left():
  sense.set_pixels(tom_pixels_left_1)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_2)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_3)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_4)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_5)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_6)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_7)
  sleep(.15)
  sense.set_pixels(tom_pixels_left_8)
  sleep(.15)
  

# Main program ------------------------
sense.clear()
while(variable):
  draw_tom_left()
