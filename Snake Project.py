from sense_hat import SenseHat # it is sense_hat when using pi
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
slug = [[2,4],[3,4],[4,4]]
color = (124, 193, 78)
direction = "right"
blank = (0,0,0)

# Functions ---------------------------
def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], color)
def move():
  
  # Find the last and first items in the slug list
  last = slug[-1]
  first = slug[0]
  next = list(last)     # Create a copy of the last item

  # Find the next pixel in the direction the slug is currently moving

  if direction == "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1

  elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1

  elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1

  elif direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1

  # Add this pixel at the end of the slug list
  slug.append(next)

  # Set the new pixel to the slug's colour
  sense.set_pixel(next[0], next[1], color)

  # Set the first pixel in the slug list to blank
  sense.set_pixel(first[0], first[1], blank)
  
  # Remove the first pixel from the list
  slug.remove(first)

def joystick_moved(event):
    global direction
    direction = event.direction


# Main program ------------------------
sense.clear()
draw_slug()
sense.stick.direction_any = joystick_moved
while True:
  move()
  sleep(0.5)
