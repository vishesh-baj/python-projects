from quiz_model import Question
from data import question_data
from quiz_brain import QuizBrain
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

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if quiz.still_has_questions() == False:
    quiz.get_final_score()









