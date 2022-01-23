with open('./file1.txt', mode='r') as first_file:
    first_list = first_file.readlines()

with open('./file2.txt', mode='r') as second_file:
    second_list = second_file.readlines()

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers that are common in both files.

first_list_fixed = [int(val.strip()) for val in first_list]
second_list_fixed = [int(val.strip()) for val in second_list]
print(first_list_fixed)
print(second_list_fixed)

in_both_files = [n for n in set(first_list_fixed).intersection(second_list_fixed)]
print(in_both_files)
