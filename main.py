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
remaining_states_x = []
remaining_states_y = []

def need_to_learn():
    """Fills a list with all the states. Said list will be used to determine what states the user needs to learn"""
    for state in state_data["state"]:
        all_states.append(state)

def check_for_state(user_guess):
    """Checks whether user's guess is a state or not"""
    for state in state_data["state"]:
        if user_guess == state:
            return True
    return False

def fill_coords(x_list, y_list):
    """Adds the necessary coordinates for the states not guessed into the 'x' or 'y' coord lists."""
    for state in all_states:
        row_for_state = state_data[state_data["state"] == state]
        x_list.append(int(row_for_state["x"]))
        y_list.append(int(row_for_state["y"]))
    print(type(x_list[1]))

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

fill_coords(remaining_states_x, remaining_states_y)

all_states_dict = {
    "State": all_states,
    "x": remaining_states_x,
    "y": remaining_states_y
}

remaining_states_df = pd.DataFrame.from_dict(all_states_dict)
print(remaining_states_df)
remaining_states_df.to_csv("states_to_learn.csv")
