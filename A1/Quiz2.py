#Quiz game: Second version
# Name: Phuong Duong
# Date: Feb 24,2026
#Make a list with the questions and correct answers.

QUESTIONS = [
    ("What is the airspeed of a laden swallow in miles per hour? ", "12"),
    ("What is the capital of Texas? ", "Austin"),
    ("The Last Super was printed by which artist ", "da Vinci"),
]
for question, correct_answer in QUESTIONS:
    answer = input(question)
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")