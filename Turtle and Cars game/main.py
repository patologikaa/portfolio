import turtle
from random import randint, choice
from turtle import Turtle, Screen
from colorgram import colorgram
from random import randint
screen = Screen()
screen.listen()
screen.setup(width=1000,height=800)
bet_winner = screen.textinput(title="Make your bet", prompt="Who win?")
colors = ["red","orange","yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []
for x in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-450, y=-200 + x * 60)
    all_turtles.append(new_turtle)
if bet_winner:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>430:
            is_race_on=False
            winner = turtle.pencolor()
            if winner==bet_winner:
                print(f"YOU WON {winner}")
            else:

                print(f"YOU LOST winner is {winner}")
        rand_distance = randint(0,50)
        turtle.forward(rand_distance)


screen.exitonclick()

