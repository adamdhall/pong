from turtle import Turtle

class Ball(Turtle):

    def __init__(self, position):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("blue")
        self.goto(position)
        self.penup()
        self.speed(5)
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed *= 0.9

    def bounce_y(self):
        self.ymove *= -1

    def reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.movespeed = 0.1