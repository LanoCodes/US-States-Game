import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(750, 550)
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Getting the state data
state_data = pd.read_csv("50_states.csv")

all_states = []
def need_to_learn():
    """Fills a list with all the states. Said list will be used to determine what states the user needs to learn"""
    for state in state_data["state"]:
        all_states.append(state)
    print(all_states)
need_to_learn()

def check_for_state(user_guess):
    """Checks whether user's guess is a state or not"""
    for state in state_data["state"]:
        if user_guess == state:
            return True
    return False

test_turtle = turtle.Turtle()
test_turtle.penup()
test_turtle.hideturtle()

total_states_guessed = 0
correct_guesses = []
need_to_learn()
while total_states_guessed != 50:
    answer_for_state = screen.textinput(title=f"{total_states_guessed}/50 States Correct", prompt="Guess a state's name:").title()

    if answer_for_state == "Exit":
        break

    if check_for_state(answer_for_state):
        print("It's a state, good job")
        row_state_guessed = state_data[state_data["state"] == answer_for_state]
        state_x_coord = int(row_state_guessed["x"])
        state_y_coord = int(row_state_guessed["y"])
        test_turtle.goto(state_x_coord, state_y_coord)
        test_turtle.write(answer_for_state, font=('Arial', 10, 'normal'))

        correct_guesses.append(answer_for_state)
        total_states_guessed += 1
        all_states.remove(answer_for_state)
        print(correct_guesses)
    else:
        print("Not quite it")

# states_to_learn.csv
# I could have a list filled with all 50 states, but whenever the user correctly guesses a state, that states gets removed from the list
