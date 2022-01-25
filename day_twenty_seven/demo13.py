import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label.pack(side='left') # use that to show the label on the screen

# v1
my_label['text'] = 'New Text'
# v2 will do the same as v1, but you can add more parameters and arguments
my_label.config(text='New Text')

window.mainloop()
