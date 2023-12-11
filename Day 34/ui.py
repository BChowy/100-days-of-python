from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizlet")

        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.q_text = self.canvas.create_text(150, 125, width=250, text="Here is the text fot the question",
                                              font=("Arial", 15, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=question)
