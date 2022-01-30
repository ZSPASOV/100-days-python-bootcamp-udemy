from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = '#fff'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(index=0, string=password)
    # the line below copies the password after generating it so you can paste it
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_username_entry.get()
    password_text = password_entry.get()


    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title='Opps', message='Do not leave empty fields.')

    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f'These are the details entered: \nEmail: {email_text} '
                                               f' \nPassword: {password_text} \nIs it ok to save?')
        if is_ok:
            with open(file='data.txt', mode='a') as file:
                file.write(f'{website_text} | {email_text} | {password_text}\n')

            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string='Password Manager')
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', bg=WHITE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text='Email/Username:', bg=WHITE)
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(index=0, string='zaprian_spasov@hotmail.com')


password_label = Label(text='Password', bg=WHITE)
password_label.grid(column=0, row=3)

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text='Generate Password', bg=WHITE, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=29, bg=WHITE, command=save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()