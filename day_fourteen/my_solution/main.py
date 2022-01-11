from art import logo
from art import vs
from game_data import data
import random


# def find_item(name):
#     filtered_item = list(filter(lambda person: person[name] == 'Ronaldinho', data))[0]
#     return filtered_item

def compare_follower_count(dict_a, dict_b, selected_option):
    if selected_option == 'A':
        return dict_a['follower_count'] > dict_b['follower_count']
    elif selected_option == 'B':
        return dict_b['follower_count'] > dict_a['follower_count']


def game():
    result = 0
    game_going_on = True
    print(logo)
    item_a = random.choice(data)
    item_b = random.choice(data)

    while game_going_on:


        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}.")
        print(vs)
        print(f"Compare B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}.")
        choice = str(input("Who has more followers? Type 'A' or 'B': "))

        outcome = compare_follower_count(dict_a=item_a, dict_b=item_b, selected_option=choice)

        if outcome == True:
            item_a = item_b
            while item_a == item_b:
                item_b = random.choice(data)
            result += 1
            print(f"You`re right! Current score: {result}")
        else:
            print(f"Sorry, that`s wrong. Final score: {result}")
            game_going_on = False


game()
