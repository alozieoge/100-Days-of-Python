import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    # for _ in range(6):
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # 35 and car.ycor() + 20 > player.ycor() > car.ycor() - 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when turtle reaches the finish line - top edge of screen
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()

    car_manager.create_car()

screen.exitonclick()
