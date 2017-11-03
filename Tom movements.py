
## This code is reponsible for the movement of the sprite utilizing the gyroscope.
## Main pitch measurement is imported from https://github.com/TeCoEd/Egg-Drop by dan_aldred

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

import time







game_over = False


basket_x = 7







'''main pitch measurement'''


def basket_move(pitch, basket_x):


   sense.set_pixel(basket_x, 7, [0, 0, 0])


   new_x = basket_x


   if 1 < pitch < 179 and basket_x != 0:


       new_x -= 1


   elif 359 > pitch > 179 and basket_x != 7:


       new_x += 1


   return new_x,







'''Main game setup'''


def main():







   basket_x = 3


     


   while game_over == False:


       pitch = sense.get_orientation()['pitch'] ##obtains gyroscope readings


       basket_x, = basket_move(pitch, basket_x) ##moves the Sprite


      


       '''Set Basket Positon'''


       sense.set_pixel(basket_x, 7, [139, 69, 19]) ## (x,y,color)


       time.sleep(0.2)


       


 












      


main()


time.sleep(1)


sense.clear()

