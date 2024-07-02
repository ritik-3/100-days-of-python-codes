from turtle import Turtle, Screen
import random

tim = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)
        
def change_colour():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)
        
for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    change_colour()

screen = Screen()
screen.exitonclick()