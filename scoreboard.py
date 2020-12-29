from turtle import Screen, Turtle


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_score

    def update_score(self):
        self.clear()
        self.goto(-150, 320)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))
        self.goto(150, 320)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))

    def score1_point(self):
        self.score1 += 1
        self.update_score()

    def score2_point(self):
        self.score2 += 1
        self.update_score()


