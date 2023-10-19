#from turtle import Turtle, Screen
import turtle as t
import random
import colorgram
"""
from turtle import *

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange")
timmy_the_turtle.forward(100)



#keep screen open
screen = Screen()
screen.exitonclick()"""
##################################
#Challenge 1
#####Turtle Intro######
"""
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############
timmy_the_turtle.speed(2)
for _ in range(4):
  timmy_the_turtle.forward(100)
  timmy_the_turtle.left(90)

timmy_the_turtle.setheading(0)
"""
########################################

##tim = Turtle()
##tom = Turtle()
##terry = Turtle()

########################################
#Challenge 2
"""tim = t.Turtle()
tim.shape("turtle")

for _ in range(5):
  tim.forward(10)
  tim.color("white")
  tim.forward(10)
  tim.color("black")

tim.left(90)

for _ in range(5):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()

screen = t.Screen()
screen.exitonclick()"""

#############################################
#Challenge 3
"""t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.speed(3)
color_random = random.Random()
sides_number = 3
figures_number = 10

def draw_shape(num_sides):
  angle = 360 / num_sides
  tim.color((color_random.randint(0, 255),
             color_random.randint(0, 255),
             color_random.randint(0, 255)))
  for _ in range(num_sides):
    tim.forward(20)
    tim.right(angle)

while figures_number != 0:
  draw_shape(sides_number)
  sides_number += 1
  figures_number -= 1

tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()

for shape_side_n in range(3, 11):
  draw_shape(shape_side_n)"""

#############################################
#Challenge 4
"""tim = t.Turtle()
tim.shape("turtle")
tim.speed(3)
tim.pensize(6)
color_random = random.Random()

def random_color():
  t.colormode(255)
  r = color_random.randint(0, 255)
  g = color_random.randint(0, 255)
  b = color_random.randint(0, 255)
  random_color = (r,g,b)
  return random_color

def turtle_direction():
  return random.choice([-270,-180,-90,0,90,180,270])

for _ in range(random.randint(1, 256)):
  tim.color(random_color())
  tim.forward(10)
  tim.setheading(turtle_direction())

times = random.randint(1,256)
while times != 0:
  tim.color(random_color())
  tim.forward(10)
  tim.setheading(turtle_direction())
  times -= 1"""

#############################################
#Challenge 5 - Spirograph
"""
tim = t.Turtle()
tim.shape("turtle")
tim.speed(20)
color_random = random.Random()

def random_color():
  t.colormode(255)
  r = color_random.randint(0, 255)
  g = color_random.randint(0, 255)
  b = color_random.randint(0, 255)
  random_color = (r,g,b)
  return random_color

def draw_spirograph2(size_of_gap, circle_size):
  for _ in range(int(360 / size_of_gap)):
    tim.setheading(tim.heading() + size_of_gap)
    tim.color(random_color())
    tim.circle(circle_size)

def draw_spirograph(size_of_gap, circle_size):
  for angle in range(360):
    if angle % size_of_gap == 0:
      tim.setheading(angle)
      tim.color(random_color())
      tim.circle(circle_size)

draw_spirograph(10, 50)
draw_spirograph2(5, 70)
"""
#############################################
#The Hirst Painting Project Part 1 - How to Extract RGB Values from Images
###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

"""rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

def colors_to_tuple_to_list(colors_list, colors):
  for color in colors:
    color_tuple = (color.rgb.r,color.rgb.g,color.rgb.b)
    colors_list.append(color_tuple)
  return colors_list

colors_list = colors_to_tuple_to_list(rgb_colors, colors)
print(colors_list)
#t.write(colors_to_tuple_to_list(rgb_colors, colors))
file = open('textx.txt','w')
file.write(f"{colors_list}")
#for item in colors_list:
#  new_item = list(item)
#  file.write(f"{new_item}\n")
file.close()"""

#################################################
#Project part Two
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), 
              (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), 
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), 
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), 
              (176, 192, 208), (168, 99, 102)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  tim.dot(20, random.choice(color_list))
  tim.forward(50)
  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()