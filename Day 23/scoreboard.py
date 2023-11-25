from turtle import Turtle
R_SCORE_POSITION = (-100, 200)
L_SCORE_POSITION = (100, 200)
ALIGNMENT = "center"
FONT = ("courier", 60, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(R_SCORE_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(L_SCORE_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
