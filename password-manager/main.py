from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{random_password}")
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    input_website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showwarning(title="Warning", message="No Data File Found")
    else:
        if input_website in data:
            email = data[input_website]["email"]
            password = data[input_website]["password"]
            messagebox.showinfo(title="Account Information", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Warning", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1)

website_search = Button(text="Search", width=15, command=find_password)
website_search.grid(column=2, row=1)

# Email / Username
email_and_username_text = Label(text="Email/Username:")
email_and_username_text.grid(column=0, row=2)

email_entry = Entry(width=53)
email_entry.insert(0, "kokona0306@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password
password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

password_generate_button = Button(text="Generate Password", command=generate_password, width=15)
password_generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
