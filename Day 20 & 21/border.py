from turtle import Turtle, Screen


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.draw_border()

    def draw_border(self):
        self.pendown()
        self.goto(280, 280)
        self.goto(280, -280)
        self.goto(-280, -280)
        self.goto(-280, 280)
