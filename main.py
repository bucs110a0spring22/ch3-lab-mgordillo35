import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('red')
leonardo.color('magenta')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.speed(1)
leonardo.speed(1)

## 5. your code goes here

michelangelo.forward(random.randrange(0,101))
leonardo.forward(random.randrange(0,101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  michelangelo.forward(random.randrange(0,11))
  leonardo.forward(random.randrange(0,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#equilateral triangle
#square (4 sides)
#hexacon (6 sides)
#nonagon (9 sides)
#dodecagon (12 sides)

# Part B - complete part B here

leonardo.hideturtle()
size_length = 30
sides_list = [3,4,6,9,12]

for i in range(sides_list[i]):
  michelangelo.pendown()
  michelangelo.forward(50)
  michelangelo.left(360/sides_list)
  michelangelo.pendown()




window.exitonclick()