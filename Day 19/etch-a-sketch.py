from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    # tim.left(10)
    angle = tim.heading() + 10
    tim.setheading(angle)


def turn_right():
    angle = tim.heading() - 10
    tim.setheading(angle)


def clear():
    tim.reset()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
