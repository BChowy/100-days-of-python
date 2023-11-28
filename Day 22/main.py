from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG game")
# Turn off animation, which we must later manually update the screen
screen.tracer(0)

screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "w")

game_is_on = True

while game_is_on:
    # Slowdown the animation/sleep between loops
    time.sleep(ball.move_speed)
    # update screen manually
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    # > 50 to make sure it's not just close to the center, but close to the paddle as a whole
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Detect if l_paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
