import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("green")

timmy.speed("fastest")
t.colormode(255)


def get_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color


# angle = 0
#
# while angle <= 360:
#     timmy.pencolor(get_color())
#     timmy.circle(100)
#     angle += 10
#     timmy.setheading(angle)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(get_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
