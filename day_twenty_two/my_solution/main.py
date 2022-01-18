import time
from turtle import Screen
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard

GAME_ENDS_AT = 5

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title(titlestring='Pong')


screen.tracer(0)


ball = Ball()


right_racket = Racket(initial_x=350, initial_y=0)
left_racket = Racket(initial_x=-350, initial_y=0)

right_scoreboard = Scoreboard(initial_x=40, initial_y=270)
left_scoreboard = Scoreboard(initial_x=-40, initial_y=270)

screen.listen()
screen.onkey(fun=right_racket.move_up, key='Up')
screen.onkey(fun=right_racket.move_down, key='Down')
screen.onkey(fun=left_racket.move_up, key='w')
screen.onkey(fun=left_racket.move_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(right_racket) < 50 and ball.xcor() > 320:
        ball.bounce_y()
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.distance(left_racket) < 50 and ball.xcor() < -320:
        ball.bounce_y()
        ball.bounce_x()

    # right paddle misses
    if ball.xcor() > 370:
        left_scoreboard.add_point()
        left_scoreboard.write_score()
        ball.reset()
        ball.bounce_x()

    # left paddle misses
    if ball.xcor() < -370:
        right_scoreboard.add_point()
        right_scoreboard.write_score()
        ball.reset()
        ball.bounce_x()

    if left_scoreboard.score == GAME_ENDS_AT or right_scoreboard == GAME_ENDS_AT:
        game_is_on = False

screen.exitonclick()