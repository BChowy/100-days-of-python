from turtle import Turtle, Screen
import random

color = ["dark khaki", "olive", "dark olive green", "olive drab", "light green", "sea green", "dark sea green",
         "medium aquamarine", "dark slate gray", "teal", "dark cyan", "cadet blue", "light sea green", "dark turquoise"]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")


def draw(sides):
    angles = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angles)


for _ in range(3, 10):
    draw(_)
    timmy.pencolor(random.choice(color))


screen = Screen()
screen.exitonclick()
