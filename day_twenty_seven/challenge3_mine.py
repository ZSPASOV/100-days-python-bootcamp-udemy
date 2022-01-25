# show as label the text written in the box when the button is clicked
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
    my_label.config(text=input.get())
button = Button(text='Click Me', command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()


window.mainloop()