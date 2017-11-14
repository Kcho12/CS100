## This code is reponsible for the movement of the sprite utilizing the gyroscope.
## Main pitch measurement is imported from https://github.com/TeCoEd/Egg-Drop by dan_aldred

from sense_hat import SenseHat
from random import randint

sense = SenseHat()
sense.clear()
import time

game_over = False

# Functions ------------------------------------------------
'''main move function to play the animation'''
def move_place():
      if pitch == 0:
        sense.set_pixels(tom_1)
      if 359 > pitch > 179:
          sense.set_pixels(tom_1)
          time.sleep(0.2)
          sense.set_pixels(tom_2)
          time.sleep(0.2)
      elif 1 < pitch < 179:
          sense.set_pixels(tom_3)
          time.sleep(0.2)
          sense.set_pixels(tom_4)          
          time.sleep(0.2)
          
## Main ----------------------------------------------------------
while game_over == False:
  pitch = sense.get_orientation()['pitch'] ##Obtains the gyroscope readings
  move_place()
  time.sleep(1)
