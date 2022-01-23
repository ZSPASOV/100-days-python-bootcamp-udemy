import pandas
import pandas as pd

data = pandas.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input()
nato_list = [nato_dict[key.upper()] for key in input_word]
print(nato_list)


