from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(*args):
    print(args)

window.after(1000, say_something, 'Hello', 'Panyo', 'wassup')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.create_line(0, 0, 0, 0)
canvas.grid(column=1, row=1)

timer_label = Label(text='Timer',bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
timer_label.grid(column=1, row=0)

start_button = Button(text='Start')
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)

# coppied the '✔' from wikipedia
tick_label = Label(text='✔', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
tick_label.grid(column=1, row=3)


# use fg to color text
window.mainloop()
