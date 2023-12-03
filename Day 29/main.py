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

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_json(new_data):
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        # Updating it with new data
        data.update(new_data)

        with open("data.json", "w") as file:
            # Write the updated data into file
            json.dump(data, file, indent=4)
    finally:
        clear_fields()


def save_password(website, email, password):
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops!", message="Please make sure to fill out all the boxes.")
    else:
        is_ok = messagebox.askokcancel(title="Check again", message=f"Is this correct?: \nWebsite: {website}"
                                                                    f"\nEmail: {email} \nPassword: {password} \nIs it "
                                                                    f"ok to save?")

        if is_ok:
            write_json(new_data)


def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def get_fields():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    save_password(website, email, password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="The file is empty. No saved passwords.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Oops!", message="No such a website saved!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.insert(0, "example@example.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=get_fields)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
