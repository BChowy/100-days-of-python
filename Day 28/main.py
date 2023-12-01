from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # config works differently on canvas, timer_text the variable we want to change
    # and text attribute is the text we change it with.
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # call count_down after 1000ms, and pass the parameter as an argument minus 1
        timer = window.after(1000, count_down, count - 1)
    else:
        #  start timer again when reaching zero
        start_timer()
        rounds = math.floor(reps / 2)
        checkmark = "✔" * rounds
        checkmark_label.config(text=checkmark)

        # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW, pady=5)
timer_label.grid(column=1, row=0)

# highlightthickness to hide canvas border
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# store it in a variable to change it later. used in count_dow function.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_btn.config(pady=2, padx=7, highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_btn.config(pady=2, padx=7, highlightthickness=0)
reset_btn.grid(column=2, row=2)

checkmark_label = Label(font=20, fg=GREEN, bg=YELLOW, pady=5)
checkmark_label.grid(column=1, row=3)

window.mainloop()
