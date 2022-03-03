from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.result = 0
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.update_screen()
        self.hideturtle()

    def update_screen(self):
        self.write(f"Score {self.result}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.result += 1
        self.clear()
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
