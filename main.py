from turtle import Turtle, Screen
from paddle1 import Paddle
from ball import Ball
from scoreboard import Score
import time

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
b = Ball()
score = Score()


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()
screen.onkeypress(p1.up, "Up")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p2.down, "s")
screen.tracer(0)

is_game_on = True
while is_game_on:
    time.sleep(b.move_speed)
    screen.update()
    b.move()

    # detect the collision of ball with the wall
    if b.ycor() > 280 or b.ycor() < -280:
        #         then it will bounce
        b.bounce_y()
    #     detect collision with paddle
    if b.distance(p1) < 20 and b.xcor() > 320 or b.distance(p2) < 20 and b.xcor() < -320:
        #         then it will bounce in opposite direction of x
        b.bounce_x()


    # detect if right paddle misses

    if b.xcor() > 380:
        b.refresh()
        score.scored_l()

    # detect if left paddle misses

    if b.xcor() < -380:
        b.refresh()
        score.scored_r()


screen.exitonclick()
