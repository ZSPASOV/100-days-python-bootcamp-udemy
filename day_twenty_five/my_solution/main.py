import turtle
import pandas
import time
import csv

screen = turtle.Screen()
screen.title('U.S. States Game')
image = './blank_states_img.gif'
screen.addshape(image)
screen.tracer(0)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# that is how to get the values of x and y coordinates of each state.
# the onscreenclick method expects as a first parameter a function with parameters x and y coordinates of the screen
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop is like screen.exitonclick() but it keeps the screen open even if you click on it
data = pandas.read_csv('./50_states.csv')
correct_guesses = 0

correctly_guessed = []
all_states = list(data['state'])

while len(correctly_guessed) < 50:
    time.sleep(0)
    screen.update()
    answer_state = screen.textinput(title=f'Correct Guesses {correct_guesses} / 50', prompt='What\'s anoter state\'s name')
    if answer_state == 'exit':
        break
    words_of_state = answer_state.split(' ')
    capitalized_words_of_state = []
    for word in words_of_state:
        capitalized_words_of_state.append(word.capitalize())

    answer_state_input = ' '.join(capitalized_words_of_state)

    filtered = data[data['state'] == answer_state_input]
    if filtered.shape[0] != 0:
        correct_guesses += 1
        x_cor = list(filtered['x'])[0]
        y_cor = list(filtered['y'])[0]
        turtle_writer = turtle.Turtle()
        turtle_writer.hideturtle()
        turtle_writer.penup()
        turtle_writer.goto(x=x_cor, y=y_cor)
        turtle_writer.write(list(filtered['state'])[0])
        correctly_guessed.append(list(filtered['state'])[0])

not_answered = list(set(all_states) - set(correctly_guessed))

with open('not_answered.csv', 'w') as file:
    writer = csv.writer(file, delimiter='\n')
    writer.writerow(not_answered)

print(f'You could not guess the following states: {not_answered}')



# turtle.mainloop()
# screen.exitonclick()