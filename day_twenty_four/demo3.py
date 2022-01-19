# mode ='w' makes the opend file writable. This overwrote the previous content in the txt file
with open(file='my_file.txt', mode='w') as file:
    file.write('New text.')

# mode = 'a' is append mode. it adds to the current content of the opened file
with open(file='other_file.txt', mode='a') as file:
    file.write('\n Metal Gear Solid')


# if we open a file that does not exist it will be created:
with open(file='new file', mode='a') as file:
    file.write('this is a new file')