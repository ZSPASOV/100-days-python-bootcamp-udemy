#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = open('./Input/Letters/starting_letter.txt')
invited_names = open('./Input/Names/invited_names.txt')


list_of_invited_names = invited_names.readlines()
list_of_invited_names_fixed = []
for name in list_of_invited_names:
    list_of_invited_names_fixed.append(name.replace('\n', ''))


starting_letter_str = starting_letter.read()

def output_email(invited_person: str):
    with open(f'./output/readytosend/email_for_{invited_person}.txt', mode='w') as file:
        file.write(starting_letter_str.replace('[name]', f'{invited_person}'))

for name in list_of_invited_names_fixed:
    output_email(name)

starting_letter.close()
invited_names.close()
