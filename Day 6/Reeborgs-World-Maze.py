# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Solution 1
# Set a limit on the number of right turns
right_turns = 0
while not at_goal():
    if right_is_clear() and right_turns < 3:
        turn_right()
        right_turns += 1
        move()
    elif front_is_clear():
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0
    # print(right_turns)
    
# Solution 2
# Make sure the robot has a wall on its right side
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
