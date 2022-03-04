from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

L_paddle = Paddle((-450, 0))
R_paddle = Paddle((450, 0))
ball = Ball()
screen.listen()
screen.onkey(L_paddle.go_up, "w")
screen.onkey(L_paddle.go_down, "s")

screen.onkey(R_paddle.go_up, "Up")
screen.onkey(R_paddle.go_down, "Down")
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # wall_collision
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    # paddle_collision

    if ball.distance(R_paddle) < 50 and ball.xcor() > 430 or ball.distance(L_paddle) < 50 and ball.xcor() < -430:
        ball.bounce_x()
    # R miss
    if ball.xcor() > 500:
        ball.reset_position()
        score.l_point()

    # L miss
    if ball.xcor() < -500:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
