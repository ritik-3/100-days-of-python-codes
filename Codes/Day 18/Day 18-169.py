from turtle import Turtle, Screen
import random

tim= Turtle()

walk = 100

def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)

for i in range(3):
    tim.forward(walk)
    tim.right(120)
change_colour()
   
for i in range(4):
    tim.forward(walk)
    tim.right(90)
change_colour()

for i in range(5):
    tim.forward(walk)
    tim.right(72)
change_colour()

for i in range(6):
    tim.forward(walk)
    tim.right(60)
change_colour()
    
for i in range(7):
    tim.forward(walk)
    tim.right(51.4285)
change_colour()

for i in range(8):
    tim.forward(walk)
    tim.right(45)
change_colour()

for i in range(9):
    tim.forward(walk)
    tim.right(40) 
change_colour()
    
for i in range(10):
    tim.forward(walk)
    tim.right(36)    
change_colour()

screen = Screen()
screen.exitonclick()