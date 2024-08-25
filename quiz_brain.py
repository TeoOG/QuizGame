class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # takes an object Question of the question_list, so concurrent_question is an object Question
        concurrent_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"q.{self.question_number}: {concurrent_question.text} (True/False): ")
        self.check_answer(user_answer, concurrent_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")
