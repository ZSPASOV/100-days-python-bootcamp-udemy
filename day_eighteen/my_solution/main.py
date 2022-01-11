import turtle
import random

import colorgram
import turtle as t

list_of_rgb = []
colors = colorgram.extract(f='damien-hirst-woodcut-esculetin-2012-for-sale.jpg', number_of_colors=100)
# colors = colorgram.extract(f='asd.jpg', number_of_colors=100)
for i in range(len(colors)):
    list_of_rgb.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

# 10 by 10 spots
# dots 20 by size , space 50 spaces
t.colormode(cmode=255)

panyo = t.Turtle()
panyo.speed(speed='fastest')
panyo.penup()
panyo.hideturtle()


def draw_dots(dost_per_row: int):
    y_position = 0

    def go_to_upper_row():
        nonlocal y_position
        y_position += 50
        panyo.goto((0, y_position))

    for _ in range(dost_per_row):

        for _ in range(dost_per_row):
            panyo.dot(20, random.choice(list_of_rgb))
            panyo.forward(distance=50)

        go_to_upper_row()


draw_dots(10)

screen = t.Screen()
screen.exitonclick()
