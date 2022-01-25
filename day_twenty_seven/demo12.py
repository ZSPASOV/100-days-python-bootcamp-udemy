# using get()
class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


# my_car = Car(make='Nissan', model='GT-R')
# print(my_car.model)

my_car = Car(make='Nissan')
print(my_car.model)
# None - using get returns None if model is not specified, but will not result in an error