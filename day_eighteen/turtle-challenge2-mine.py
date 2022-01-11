from turtle import Turtle, Screen

panyo = Turtle()
for _ in range(20):
    panyo.pendown()
    panyo.forward(distance=10)
    panyo.penup()
    panyo.forward(distance=10)


screen = Screen()
screen.exitonclick()


