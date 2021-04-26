import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_turtle = turtle.Turtle()
state_turtle.hideturtle()

# Import 50 states data
data = pd.read_csv("50_states.csv")
num_states = len(data)
# print(data["state"])

game_on = True
correct_guesses = []
score = 0
game_title = "Guess the State"

# 4. Use a loop to allow the user keep guessing.
while game_on:

    answer_state = screen.textinput(title=f"{game_title}", prompt="What's another state's name?")
    # print(answer_state)

    # 1. Convert the guess to Title case.
    answer_state = answer_state.title()

    # 2. Check if the guess is among the 50 states.
    is_correct_guess = False
    state_data = data[data["state"] == answer_state]
    # print(state_data)

    if len(state_data) != 0:
        is_correct_guess = True

        # 3. Write the correct guess onto the map.
        state_turtle.penup()
        state_turtle.goto((int(state_data["x"]), int(state_data["y"])))
        state_turtle.pendown()
        state_turtle.write(answer_state, align="left")

        # 5. Record the correct guesses in a list
        correct_guesses.append(answer_state)

        # 6. Keep track of the score.
        score += 1
        game_title = f"{score}/{num_states}"


# Completed, data already generated.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() # alternative to screen.exitonclick() without exiting the screen on mouse click

# screen.exitonclick()
