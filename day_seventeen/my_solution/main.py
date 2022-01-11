from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for el in question_data:
    values_of_el = list(el.values())
    question_bank.append(Question(text=values_of_el[0], answer=values_of_el[1]))

quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()