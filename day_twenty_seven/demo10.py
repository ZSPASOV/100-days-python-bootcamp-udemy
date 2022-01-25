class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']


my_car = Car(make='Nissan', model='GT-R')
print(my_car.model)