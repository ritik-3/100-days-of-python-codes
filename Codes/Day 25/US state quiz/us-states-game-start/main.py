import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "C:\Coading\Python\Python 100 Days\Day 25\US state quiz\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:\Coading\Python\Python 100 Days\Day 25\US state quiz\us-states-game-start\50_states.csv")
all_states = data.state.to_list()
guesses_state = []


while len(guesses_state) < 50:
        
    answer_state = screen.textinput(title=f"{len(guesses_state)}//50 States correct", prompt="What's another stats name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guesses_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guesses_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x, state_data.y))
        t.write(answer_state)
        
screen.exitonclick()