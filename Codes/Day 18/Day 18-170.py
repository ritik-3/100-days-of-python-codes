from turtle import Turtle, Screen
import random

tim= Turtle()
tim.pensize(6)

turns = [0, 90, 180, 270]

def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)

for i in range(200):
    tim.forward(30)
    tim.setheading(random.choice(turns))
    change_colour()    


screen = Screen()
screen.exitonclick()