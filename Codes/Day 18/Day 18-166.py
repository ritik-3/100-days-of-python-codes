from turtle import Turtle, Screen

timmy = Turtle()
walk = 100

timmy.pencolor("red")
for run in range(4):
    timmy.forward(walk)
    timmy.right(90)



screen = Screen()
screen.exitonclick()