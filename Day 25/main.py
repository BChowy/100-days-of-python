import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                              prompt="Guess a State name:").title()  # Convert the string to title case

    if answer == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        # missed_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        state_data = data[data["state"] == answer]
        text.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
        text.write(state_data["state"].item())
        guessed_states.append(answer)

