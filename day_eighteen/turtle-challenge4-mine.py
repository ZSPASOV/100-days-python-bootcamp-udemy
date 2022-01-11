import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
directions = ['backward', 'forward']
angles = [0, 90, 180, 270]

tim.shape(name='arrow')
tim.speed(speed=8)
tim.width(width=25)
t.colormode(cmode=255)

def walk_randomly(number_steps: int, walking_turtle: object):

    for _ in range(number_steps):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        # selected_colour = random.choice(colours)
        selected_direction = random.choice(directions)
        selected_angle = random.choice(angles)
        walking_turtle.color((red, green, blue))
        if selected_direction == 'backward':
            walking_turtle.right(angle=selected_angle)
            walking_turtle.backward(distance=50)
        elif selected_direction == 'forward':
            walking_turtle.right(angle=selected_angle)
            walking_turtle.forward(distance=50)

walk_randomly(number_steps=100, walking_turtle=tim)
