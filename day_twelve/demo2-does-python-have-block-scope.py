# There is no Block Scope

game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# in a function there is local scope
def create_enemy():
    enemies = ['Skeleton', 'Zombie', 'Alien']
    if game_level < 5:
        new_enemy_selected = enemies[0]
        print(new_enemy_selected)

# print(new_enemy_selected) NameError: name 'new_enemy_selected' is not defined

# If you create a variable within a function it is only available in that function.
# If you create a variable in an if block or in a loop, this does not count as creating a separate local scope
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.