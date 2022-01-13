# examples from the quiz
# question 1
class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        self.temperament = 'outgoing'

# Correct. The call to super() in the initialiser is recommended, but not strictly required.

