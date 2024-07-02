from turtle import Turtle,Screen
import random
is_race_on= False

new_turtle = Turtle()
screen = Screen()

screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Choose the colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtule is winner!")
            else:
                print(f"You have lost! The {winning_color} turtule is winner!")
                
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick() 