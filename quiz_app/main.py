from quiz_model import Question
from data import question_data

# question bank list
def create_question_bank(question_data):
    question_bank = []
    for question in question_data:
        question_text = question['text']
        question_answer = question['answer']
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank

question_bank = create_question_bank(question_data)

score = 0

for i in question_bank:
    print(i.text)
    answer = input("Enter True or False")
    if answer == i.answer:
        score += 1
        print("Correct")
    else:
        score -= 1
        print("Incorrect")
        
    





    




















