import turtle as t
import colorgram
import random

t.colormode(255)

timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

# colors = colorgram.extract('hirst-painting.jpg', 20)
#
#
# def extract_rgb(colors_list):
#     rgb_colors = []
#     for color in colors_list:
#         r = color.rgb.r
#         b = color.rgb.b
#         g = color.rgb.g
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#     return rgb_colors

colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
          (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123),
          (200, 121, 143), (168, 21, 29), (228, 92, 77)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

dots_number = 100

for dot_count in range(1, dots_number + 1):
    timmy.dot(20, random.choice(colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = t.Screen()
screen.exitonclick()
