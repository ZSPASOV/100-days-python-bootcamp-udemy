from turtle import Turtle, Screen
import random

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# each of them with random color, each figure on top of the other

# my solution
COLORS = ["blue", "black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
panyo = Turtle()
# a triangle

def draw_figure(number_of_sides: int, drawing_turtle: object):
    random_color = random.choice(COLORS)
    # red = random.randint(0, 255)
    # green = random.randint(0, 255)
    # blue = random.randint(0, 255)
    drawing_turtle.color(random_color)
    for _ in range(number_of_sides):
        drawing_turtle.forward(distance=100)
        drawing_turtle.right(angle=360 / number_of_sides)


for i in range(3, 11):
    draw_figure(number_of_sides=i, drawing_turtle=panyo)




screen = Screen()
screen.exitonclick()
