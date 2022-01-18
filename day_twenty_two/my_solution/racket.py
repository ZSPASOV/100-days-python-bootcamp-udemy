from turtle import Turtle

class Racket(Turtle):
    def __init__(self, initial_x: int, initial_y: int):
        super().__init__()
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.hideturtle()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.goto(x=self.initial_x, y=self.initial_y)
        self.showturtle()

    def move_up(self):
        ycor = self.ycor()
        self.goto(x=self.initial_x, y=ycor + 20)

    def move_down(self):
        ycor = self.ycor()
        self.goto(x=self.initial_x, y=ycor - 20)
