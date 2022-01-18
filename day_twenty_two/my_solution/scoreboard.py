from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, initial_x, initial_y):
        super().__init__()
        self.score = 0
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.hideturtle()
        self.goto(x=initial_x, y=initial_y)
        self.write_score()

    def add_point(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(arg=f"{self.score}", align='center', font=('Verdana', 16, 'bold'))