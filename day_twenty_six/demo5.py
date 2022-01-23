import random
names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
