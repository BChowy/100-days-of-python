from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you pet", prompt="Which turtle will win the race?(red/orange/blue/purple)")
colors = ["red", "orange", "blue", "purple"]

is_race_on = False
all_turtles = []
y_position = -70

for turtles_number in range(0, len(colors)):
    a_turtle = Turtle(shape="turtle")
    a_turtle.penup()
    a_turtle.color(colors[turtles_number])
    a_turtle.goto(x=-230, y=y_position)
    y_position += 50
    all_turtles.append(a_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you've won The {winner} turtle is the winner")
            else:
                print(f"you've lost The {winner} turtle is the winner")

        speed = random.randint(0, 30)
        turtle.forward(speed)

screen.exitonclick()
