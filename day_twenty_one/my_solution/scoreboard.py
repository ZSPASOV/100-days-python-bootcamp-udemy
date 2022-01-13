from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.goto(0, 282)

    def add_point(self):
        self.score += 1

    def reset_score(self):
        self.score = 0


