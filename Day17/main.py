from question_model import Question
from data import question_data

question_bank = []

for question in question_bank:
    question_text = question["text"]
    answer = question["answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)
