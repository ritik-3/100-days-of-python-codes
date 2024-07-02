from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

all_turtle = []
x_positions = [0, -20, -40]

for turtle_index in range(0, 3):
    new_turtle = Turtle()
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(y=0 , x=x_positions[turtle_index])
    all_turtle.append(new_turtle)
 
















screen.exitonclick()