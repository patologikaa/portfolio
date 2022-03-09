import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
guessed = []
while score < 50:
    answer_state = screen.textinput(title=f"Guess the state {score}/50", prompt="What's the name of the state?").title()
    data = pandas.read_csv("50_states.csv")
    state_pointed = data[data["state"] == answer_state]
    if answer_state == "Exit":
        break
    if (len(state_pointed)) > 0:
        guessed.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_pointed.x), int(state_pointed.y))
        t.write(str(state_pointed.state.item()))

to_export = []

for st in pandas.read_csv("50_states.csv").state:
    if st not in guessed:
        to_export.append(st)

new_data = pandas.DataFrame(to_export)
new_data.to_csv("states_to_learn.csv")