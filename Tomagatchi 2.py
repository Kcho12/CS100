from sense_hat import SenseHat
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
tom = [[1,4],[2,6],[2,5],[2,4],[2,3],[3,4],[3,3],[2,4],[2,3],[4,3],[4,4],[5,6],[5,5],[5,4],[5,3],[5,2],[5,1],[6,2]]

# Functions ---------------------------
def draw_tom():
    for segment in tom:
        sense.set_pixel(segment[0], segment[1], br)

# Main program ------------------------
sense.clear()
draw_tom()
