from turtle import Turtle, Screen

panyo = Turtle()
for _ in range(4):
    panyo.forward(distance=100)
    panyo.right(angle=90)

screen = Screen()
screen.exitonclick()