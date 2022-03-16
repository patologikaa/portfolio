from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = web_entry.get()
    mail = mail_entry.get()
    passwd = pass_entry.get()

    new_data = {
        web: {
            "mail": mail,
            "password": passwd
        }
    }
    if len(web) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Error", message="Please fill all inputs")
    else:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
#-----------------------FIND PASSWORD --------------------------- #
def searchService():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"There's no database file")

    else:
        service = web_entry.get()
        if service in data:
            data_pass = data[service]["password"]
            data_mail = data[service]["mail"]
            messagebox.showinfo(title="Password", message=f"Your mail is: {data_mail} \n Your password is: {data_pass}")
        else:
            messagebox.showinfo(title="Error", message=f"No such service")

# ---------------------------- UI SETUP ------------------------------- #

web = Label(text="Website ")
mail = Label(text="Mail/Login")
password = Label(text="Password ")
generate = Button(text="Generate", width=10, command=generate)
add = Button(text="Add", width=25, command=add)
search = Button(text="Search", width=10, command=searchService)
web_entry = Entry(width=30)

web_entry = Entry(width=32)
mail_entry = Entry(width=45)
pass_entry = Entry(width=32)

web.grid(column=0, row=1)
web_entry.grid(column=1, row=1)
web_entry.focus()

mail.grid(column=0, row=2)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "yourEmal@gmail.com")

password.grid(column=0, row=3)
pass_entry.grid(column=1, row=3)

add.grid(column=1, row=4)
generate.grid(column=2, row=3)
search.grid(column=2,row=1)

window.mainloop()
