from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

tim = Turtle(shape='turtle')
tim.setheading(to_angle=180)
tim.color('red')
print(tim.color()[0])


screen.exitonclick()