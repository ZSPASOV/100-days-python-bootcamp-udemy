# Modifying Global Scope
enemies = 5

def increase_enemies():
    global enemies
    enemies += 1
    print(f'enemies are: {enemies}')

increase_enemies()
print(enemies)

# this however is a not a good idea. it is a bad practice to modify variables in the global scope.

# this is the better way

other_enemies = 2

def increase_other_enemies():
    print(f'enemies inside the function: {other_enemies}')
    return other_enemies + 1

other_enemies = increase_other_enemies()
print(f'enemies outside the function: {other_enemies}')