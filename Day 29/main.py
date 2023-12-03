from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password(website, email, password):
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")


def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def get_fields():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    save_password(website, email, password)
    clear_fields()


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

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.insert(0, "example@example.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, command=get_fields)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
