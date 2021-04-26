import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} states correct",
                                    prompt="What's another U.S. state's name?").title()
    print(answer_state)

    # Check for exit password
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # print(missed_states)
        # print(len(missed_states))
        # Write the missing states to states_to_learn.csv
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # If answer_state is one of the states in all the states in 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # Create a turtle to write the name of the state at the state's x and y coordinates
        t = turtle.Turtle()
        t.pencolor("black")
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
        # t.write(state_data["state"].item())

# turtle.mainloop()
