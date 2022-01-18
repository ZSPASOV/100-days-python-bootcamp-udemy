from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = CarManager()
            car.shape(name='square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(to_angle=180)
            car.goto(x=300, y=random.randint(-250, 250))
            self.list_of_cars.append(car)


    def move(self):
        for car in self.list_of_cars:
            car.forward(distance=self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT