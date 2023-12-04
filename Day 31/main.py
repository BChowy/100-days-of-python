from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

current_card = {}
words_dict = {}

try:
    data_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data_file.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(words_dict)
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    # False so it doesn't add their record number everytime causing repeating in the file indexes
    data.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Cards")
window.maxsize(width=900, height=726)
window.minsize(width=900, height=726)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="", font=(FONT_NAME, 35, "italic"))
word = canvas.create_text(400, 265, text="", font=(FONT_NAME, 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=1, row=1)

next_card()
window.mainloop()
