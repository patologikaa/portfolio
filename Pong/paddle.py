from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.speed("fastest")
        self.shape("square")
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 20)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y - 20)
