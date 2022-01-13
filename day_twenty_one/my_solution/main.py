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
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
scoreboard.write(arg=f"Score: {scoreboard.score}", align='center', font=('Verdana', 10, 'bold'))
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.clear()
        scoreboard.add_point()
        scoreboard.write(arg=f"Score: {scoreboard.score}", align='center', font=('Verdana', 10, 'bold'))
        snake.grow()

        food.refresh()

    # Detect collision with walls.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.goto(x=0, y=0)
        scoreboard.write(arg=f"GAME OVER", align='center', font=('Verdana', 20, 'bold'))

    # detect collision with tail
    # v1
    # for seg in snake.segments:
    #     if snake.segments.index(seg) != 0 and seg.distance(snake.head) < 10:
    #         game_is_on = False
    #         scoreboard.goto(x=0, y=0)
    #         scoreboard.write(arg=f"GAME OVER", align='center', font=('Verdana', 20, 'bold'))
    # v2 with slicing
    for seg in snake.segments[1:]:
        if seg.distance(snake.head) < 10:
            game_is_on = False
            scoreboard.goto(x=0, y=0)
            scoreboard.write(arg=f"GAME OVER", align='center', font=('Verdana', 20, 'bold'))



screen.exitonclick()