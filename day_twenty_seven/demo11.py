# notice the error when the model argument is not specified
class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']


# my_car = Car(make='Nissan', model='GT-R')
# print(my_car.model)

my_car = Car(make='Nissan')
print(my_car.model)

# Traceback (most recent call last):
#   File "E:\programming\python\Udemy one hundred days python\problems\day_twenty_seven\demo11.py", line 11, in <module>
#     my_car = Car(make='Nissan')
#   File "E:\programming\python\Udemy one hundred days python\problems\day_twenty_seven\demo11.py", line 5, in __init__
#     self.model = kw['model']
# KeyError: 'model'