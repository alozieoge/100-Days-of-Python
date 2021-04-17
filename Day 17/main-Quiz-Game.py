from question_model import Question
# from data import question_data
from data_otb import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # question_text = question["text"]
    # question_answer = question["answer"]
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
# print(quiz.question_number)
# print(quiz.question_list[0])

while quiz.still_has_questions():
    quiz.next_question()
# quiz.end_game()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
