# with absolute path
# note - the real absolute path should be /Users/lenovo/day_twenty_four.txt but since we are on E drive we have to reach it like below
with open(file=r'C:\Users\lenovo\day_twenty_four.txt') as file:
    check = file.read()
    print(check)

# with relative path
with open('../../day_twenty_four_challenge.txt') as file:
    check = file.read()
    print(check)

with open('..\..\day_twenty_four_challenge.txt') as file:
    check = file.read()
    print(check)

# check whether absolute path with windows \ slashes work
# with open('E:\programming\python\Udemy one hundred days python\day_twenty_four_challenge.txt') as file:
#     check = file.read()
#     print(check)

# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 21-24: truncated \UXXXXXXXX escape


# absolute file path is always relevant to the root of your computer. On Windows it is the C drive, unless you changed it.
# the relative file path is relative to your current working directory.