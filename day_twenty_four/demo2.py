# when opening a file using WITH it closes automatically, you don`t need to use file.close()
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)