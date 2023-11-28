from turtle import Turtle

MOVEMENT_SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        # Make width 100 and length default 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_down(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def move_up(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)
