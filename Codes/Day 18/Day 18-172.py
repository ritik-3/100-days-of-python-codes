from turtle import Turtle, Screen
import random

tim= Turtle()
tim.speed("fastest")
def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)


def draw_spirograph(size_of_gap):
    for i in range(int(360/ size_of_gap)):
        tim.circle(100)
        tim.left(size_of_gap)
        change_colour()
 
draw_spirograph(7)

screen = Screen()
screen.exitonclick()