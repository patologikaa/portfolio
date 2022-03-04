from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.x_move, y + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
