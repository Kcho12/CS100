from sense_hat import SenseHat # it is sense_hat when using pi
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
slug = [[2,4],[3,4],[4,4]]
color = (124, 193, 78)
color_two = (255,0,0)
direction = "right"
blank = (0,0,0)
vegetables = []
score = 0
pause = 0.5
dead = False

# Functions ---------------------------
def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], color)
        
def move():
  global score
  global pause
  global dead

  remove = True
  
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

  if next in slug:
      dead = True
      sense.show_message("Game Over")
      sense.show_message(":)")

  # Add this pixel at the end of the slug list
  slug.append(next)

  # Set the new pixel to the slug's colour
  sense.set_pixel(next[0], next[1], color)

  if next in vegetables:
      vegetables.remove(next)
      score += 1
      if ((score % 5) == 0):
        remove = False
        pause = pause * 0.7

  if remove:
      sense.set_pixel(first[0], first[1], blank)
      slug.remove(first)

def joystick_moved(event):
    global direction
    direction = event.direction
    
def make_veg():
    new = slug[0]
    while new in slug:
        x = randint(0,7)
        y = randint(0,7)
        new = [x,y]
        vegetables.append(new)
        sense.set_pixel(x, y, color_two)


# Main program ------------------------
sense.clear()
draw_slug()
sense.stick.direction_any = joystick_moved
while (dead==False):
    if len(vegetables) < 3 and randint(1, 5) > 4:
        make_veg()
    move()
    sleep(pause)
