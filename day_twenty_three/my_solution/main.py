import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(fun=player.move, key='Up')

car_manager = CarManager()
car_manager.hideturtle() # if i dont want to invoke that i just need to use car = CarManager() in the car_manager create_car() method

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # car reaches end
    if player.ycor() == FINISH_LINE_Y:
        scoreboard.increase_level()
        scoreboard.write_level()
        car_manager.increase_speed()
        player.reset()

    # detect a colision with a car
    for car in car_manager.list_of_cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()

