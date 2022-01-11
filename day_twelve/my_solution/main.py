import random
# from replit import clear
from art import logo

LOWER_RANGE = 1
UPPER_RANGE = 100

def attempts():
    print(logo)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5

number_attempts = attempts()

random_num = random.choice(range(LOWER_RANGE, UPPER_RANGE))
# print(f'Pssst, the correct answer is {random_num}')


while number_attempts > 0:
    print(f'You have {number_attempts} attempts remaining to guess the number.')
    number_attempts -= 1
    selected_number = int(input('Make a guess: '))
    if selected_number == random_num:
        print(f'You got it! The answer was {random_num}')
        break
    elif selected_number < random_num:
        print('Too low.\nGuess again.')
    else:
        print('Too high.\nGuess again.')
    if number_attempts == 0:
        print("You've run out of guesses, you lose.")




