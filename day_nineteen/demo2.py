def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# calculator is a higher order function. it takes another function as an input
# this is very useful when you need to listen to events, for example
def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(2, 3, divide)
print(result)

result2 = calculator(2, 3, add)
print(result2)