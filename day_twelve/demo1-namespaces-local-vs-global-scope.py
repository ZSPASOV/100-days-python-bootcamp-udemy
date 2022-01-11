################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strength = 5
  print(potion_strength)

drink_potion()
# print(potion_strenth)  NameError: name 'potion_strenth' is not defined

# Global Scope
player_health = 10

def drink_potion_again():
  potion_strength = 2
  print(player_health)

drink_potion_again()

def game():
  def drink_other_potion():
    potion_strength = 2
    print(player_health)

  drink_other_potion()

game()