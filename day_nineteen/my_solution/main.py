from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
selected_color = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-80, -40, -0, 40, 80, 120]
list_of_turtles = []
game_is_running = True

for turtle_index in range(0, 6):
    created_turtle = Turtle(shape='turtle')
    created_turtle.color(colors[turtle_index])
    created_turtle.penup()
    created_turtle.goto(x=-230, y=y_positions[turtle_index])
    list_of_turtles.append(created_turtle)

while game_is_running:
    for current_turtle in list_of_turtles:
        random_step = random.randint(0, 10)
        current_turtle.forward(distance=random_step)
        if current_turtle.xcor() >= 200:
            game_is_running = False
            if current_turtle.color()[0] == selected_color:
                print(f"You have guessed. The {selected_color} won.")
            else:
                print(f"You did not guess. The {current_turtle.color()[0]} won.")



screen.exitonclick()