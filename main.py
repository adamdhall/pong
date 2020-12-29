from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
divider = Turtle()


screen.bgcolor("black")
screen.screensize(800, 800)
screen.tracer(0)
screen.title("Pong")
screen.listen()

paddle1 = Paddle((-390, 0))
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

paddle2 = Paddle((390, 0))
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")


divider.penup()

ball = Ball((0, 0))
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:

    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    scoreboard.update_score()


    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.bounce_y()

#detect collision w/ right paddle
    if ball.distance(paddle2) < 50 and ball.xcor() > 340 or ball.distance(paddle1) < 50 and ball.xcor() < -340:
        ball.bounce_x()


#detect ball going past paddle
    if ball.xcor() > 450:
        scoreboard.score1_point()
        ball.reset()

    elif ball.xcor() < -450:
        scoreboard.score2_point()
        ball.reset()

    if scoreboard.score1 > 5 or scoreboard.score2 > 5:
        print("you win!")
        game_is_on = False

screen.exitonclick()
