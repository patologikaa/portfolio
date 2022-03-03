import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.randint(-350, 350)
        rand_y = random.randint(-350, 350)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(-350, 350)
        rand_y = random.randint(-350, 350)
        self.goto(rand_x, rand_y)
