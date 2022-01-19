class QuizBrain:


    def __init__(self, question_lst):
        self.score = 0
        self.question_num = 0
        self.question_lst = question_lst


    def still_has_questions(self):
        return self.question_num < len(self.question_lst) 
           

    def next_question(self):
        question = self.question_lst[self.question_num]
        user_answer = input(f"Q-{self.question_num + 1} {question.text} (True or False?): ")
        self.check_answer(user_answer, question.answer)
        self.question_num += 1

    
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct answer, your score is {self.score}/{self.question_num}")

        else:
            print("Incorrect answer")

        print(f"Correct answer is {self.question_lst[self.question_num].answer}")
        print("\n")

    def get_final_score(self):
        print(f"Your final score is: {self.score}/12")








