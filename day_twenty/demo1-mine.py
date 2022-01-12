from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title(titlestring='My Snake Game')

list_of_turtles = []
x_axis = [0, -20, -40]



for i in range(3):
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.goto(x=x_axis[i], y = 0)
    list_of_turtles.append(new_turtle)

screen.exitonclick()