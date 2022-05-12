from turtle import Turtle


class Life(Turtle):

    def __init__(self):
        super().__init__()
        self.color("coral")
        self.penup()
        self.hideturtle()
        self.l_life = 3
        self.r_life = 3
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(-338, 270)
        self.write(f"Life: {self.l_life}", align="center", font=("courier", 20, "bold"))
        self.goto(338, 270)
        self.write(f"Life: {self.r_life}", align="center", font=("courier", 20, "bold"))

    def decrease_l_life(self):
        self.l_life -= 1
        self.update_life()

    def decrease_r_life(self):
        self.r_life -= 1
        self.update_life()
