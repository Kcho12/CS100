from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
Slug = [[2,4],[3,4],[4,4]]
Green=(124,193,78)

# Functions ---------------------------
def draw_slug():
        for segment in Slug:
                sense.set_pixel(segment[0], segment[1], Green)

# Main program ------------------------
sense.clear()
draw_slug()


