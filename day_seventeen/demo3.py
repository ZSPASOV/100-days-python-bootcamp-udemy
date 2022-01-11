class Car:

    def __init__(self, seats):
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2

car = Car(seats=5)
car.enter_race_mode()
print(car.seats)