from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.result = 0
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 350)
        self.update_screen()
        self.hideturtle()


    def update_screen(self):
        self.clear()
        self.write(f"Score: {self.result} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.result += 1
        self.update_screen()

    def reset(self):
        if self.result > self.high_score:
            with open('high_score.txt','w') as f:
                f.write(str(self.result))
            self.high_score = self.result
        self.result = 0
        self.update_score()

