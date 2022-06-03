from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

r_marks = 0
l_marks = 0

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce('x')
        print(ball.xcor())

    if (ball.xcor() > 330 or ball.xcor() < -330) and (ball.distance(r_paddle) > 50 or ball.distance(l_paddle) > 50):
        if ball.xcor() > 330 and (ball.distance(r_paddle) > 50):
            ball.reset_position()
            scoreboard.l_point()

        elif ball.xcor() < -330 and (ball.distance(l_paddle) > 50):
            ball.reset_position()
            scoreboard.r_point()

screen.exitonclick()
