from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("A Pong Game")
screen.tracer(0)

score = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Close program when Escape key is pressed, alternative exit method until game is complete
screen.onkey(screen.bye, "Escape")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
