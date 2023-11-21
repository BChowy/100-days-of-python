import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("green")

timmy.pensize(15)
direction = [0, 90, 180, 270]
timmy.speed("fastest")
t.colormode(255)


def get_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color


for _ in range(200):
    timmy.color(get_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = t.Screen()
screen.exitonclick()
