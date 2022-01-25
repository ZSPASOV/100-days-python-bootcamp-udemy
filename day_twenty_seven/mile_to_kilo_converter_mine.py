from tkinter import *

def click_button():
    km_value = int(miles_value.get()) * 1.609344
    km_converted_label.config(text=int(km_value))

window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=200, height=200)

miles_value = Entry()
miles_value.grid(column=1, row=0)

miles_label = Label(text='Miles')

is_equal_to_label = Label(text='is qual to')
is_equal_to_label.grid(column=0, row=1)

km_converted_label = Label(text='0')
km_converted_label.grid(column=1,  row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=click_button)
button.grid(column=1, row=2)

window.mainloop()

