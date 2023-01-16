from turtle import Screen, Turtle

import pandas
import pandas as pd

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()


score_count = 0
correct_guesses = []
should_continue = True


while should_continue:

    answer_state = screen.textinput(title=f"{score_count}/50 states correct",
                                    prompt="What's another states name?").title()
    if answer_state == "exit":
        missing_states = [state for state in all_states if state not in correct_guesses]

        # missing_states = []
        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_states.append (state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        score_count += 1
        state_row=(data[data["state"] == answer_state])
        state_x=int(state_row["x"])
        state_y=int(state_row["y"])

        state_object=Turtle()
        state_object.hideturtle()
        state_object.penup()
        state_object.goto(state_x, state_y)
        state_object.write(answer_state)

    # else:
    #     should_continue = False
    #     game_over = Turtle()
    #     game_over.hideturtle()
    #     game_over.write(arg=f"GAME OVER. Your score = {score_count}", align="center", font=("Verdana",
    #                                 15, "normal"))


screen.exitonclick()
