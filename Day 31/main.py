from tkinter import *



BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flash Cards")
window.maxsize(width=900, height=726)
window.minsize(width=900, height=726)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="", font=(FONT_NAME, 35, "italic"))
word = canvas.create_text(400, 265, text="", font=(FONT_NAME, 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(column=0, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(column=1, row=1)

window.mainloop()
