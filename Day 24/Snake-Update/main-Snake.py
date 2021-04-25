from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()  # food is a Turtle object since the Food class inherits from the Turtle class.
scoreboard = Scoreboard()  # scoreboard is also a Turtle object since Scoreboard inherits from Turtle.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 2. Move the snake forwards by default.
# Starting from the last segment, move each segment to the position of the segment ahead.
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food using turtle.distance()
    # Which returns the distance between two turtles.
    if snake.head.distance(food) < 15:  # If the snake head is within 15 pixels of the food
        # print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset_scoreboard()
        scoreboard.save_high_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # If head collides any segment in the tail:
        # trigger game over sequence
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset_scoreboard()
            scoreboard.save_high_score()
            snake.reset_snake()


screen.exitonclick()
