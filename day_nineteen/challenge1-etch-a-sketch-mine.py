from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

screen.listen()


# W forwards
# S Backwards
# A counter-clockwise
# D clockwise
# C clear drawing

def move_forward():
    tim.forward(distance=10)

def move_backwards():
    tim.backward(distance=10)

def move_counter_clockwise():
    tim.left(angle=10)

def move_clockwise():
    tim.right(angle=10)

def clear_drawing():
    screen.clearscreen()

screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=move_counter_clockwise)
screen.onkeypress(key='d', fun=move_clockwise)
screen.onkeypress(key='c', fun=clear_drawing)


screen.exitonclick()
