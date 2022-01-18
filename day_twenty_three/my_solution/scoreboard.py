import turtle
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=250)
        self.level = 0
        self.write_level()


    def write_level(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='Game Over', font=FONT, align='center')

