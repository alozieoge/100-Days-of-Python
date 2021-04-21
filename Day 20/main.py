from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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
    if snake.head.distance(food) < 15:  # If the snake head is within 15 pixels of the food or closer
        # print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall (boundary)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # If head collides any other segment in the tail:
        # trigger game over sequence
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
