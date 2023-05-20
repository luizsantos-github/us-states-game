import turtle
import pandas

# Program Breakdown
# Convert the guess to Title Case - DONE
# Write correct guesses onto the map - DONE
# Use a loop to allow the user to keep guessing - DONE
# Record the correct guesses in a list
# Keep track of the score

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Data Consumption
df = pandas.read_csv("50_states.csv")

# Compose Data
states_plot = {}
for index, row in df.iterrows():
    states_plot[row.state] = (row.x, row.y)

total_score = len(states_plot)
correct_score = 0
guessed_states = []
missed_states = []

while correct_score < 50:
    answer_state = screen.textinput(title=f"{correct_score}/{total_score} Guess the state", prompt="What's another state name?").title()

    # Create a csv that will list out all missed states
    if answer_state == "Exit":
        for state in states_plot:
            if state not in guessed_states:
                missed_states.append(state)
        missed_data = pandas.DataFrame(missed_states)
        missed_data.to_csv('states_to_learn')
        break
    # Plot the correctly guessed state in the map
    if answer_state in states_plot:
        show_state = turtle.Turtle()
        show_state.penup()
        show_state.hideturtle()
        show_state.goto(states_plot[answer_state])
        show_state.write(answer_state, align="center", font=("Courier", 8, "normal"))
        correct_score += 1
        guessed_states.append(answer_state)

screen.exitonclick()
