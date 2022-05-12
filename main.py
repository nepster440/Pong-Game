from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from life import Life
import time


class UserInput(Turtle):

    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_input()

    def user_input(self):
        self.goto(-200, 245)
        self.player1 = screen.textinput(title="Player Name", prompt="Enter your name: ")
        self.write(f"Player1: {self.player1}", align="center", font=("courier", 15, "bold"))

        self.goto(200, 245)
        self.player2 = screen.textinput(title="Player Name", prompt="Enter your name: ")
        self.write(f"Player2: {self.player2}", align="center", font=("courier", 15, "bold"))

    def winner_l_paddle(self):
        self.goto(0, 0)
        self.write(f"Winner: {self.player1}", align="center", font=("courier", 50, "bold"))

    def winner_r_paddle(self):
        self.goto(0, 0)
        self.write(f"Winner: {self.player2}", align="center", font=("courier", 50, "bold"))

    def draw_game(self):
        self.goto(0, 0)
        self.write(f"Match a Draw!", align="center", font=("courier", 50, "bold"))


screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
life = Life()
player = UserInput()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_point()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        scoreboard.l_point()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        life.decrease_r_life()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        life.decrease_l_life()

    # Game Over
    if life.l_life == 0 or life.r_life == 0:
        if scoreboard.l_score == scoreboard.r_score:
            game_is_on = False
            player.draw_game()
        elif scoreboard.l_score < scoreboard.r_score:
            game_is_on = False
            player.winner_r_paddle()
        else:
            player.winner_l_paddle()

# screen.mainloop()
screen.exitonclick()
