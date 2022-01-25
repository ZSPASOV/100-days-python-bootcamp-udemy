# show the 'button got clicked' on my_label when the button get`s clicked
from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label

my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack() # use that to show the label on the screen

# v1
my_label['text'] = 'New Text'
# v2 will do the same as v1, but you can add more parameters and arguments
my_label.config(text='New Text')

# Button

def button_clicked():
    my_label.config(text='Button Got Clicked')
button = Button(text='Click Me', command=button_clicked)
button.pack()


window.mainloop()