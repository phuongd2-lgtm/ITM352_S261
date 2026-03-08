#Name: Phuong Duong
#Date: Mar 2nd,2026

# Assignment 1
# Quiz Application
# Extra requirements used:
# 1) Write score history to a file
# 10) 50/50 feature usable once per game

import json
from datetime import datetime

# load questions from file
with open("questions.json", "r") as file:
    questions = json.load(file)

name = input("Enter your name: ")
score = 0
used_fifty = False

print("\nWelcome to the NBA Quiz!")
print("There are 5 questions for you to answer.")
print("Type a, b, c, or d.")
print("You can type 50 one time to remove two wrong answers.\n")

for q in questions[:5]:
    print(q["question"])

    # create dictionary for choices
    choices = {
        "a": q["options"][0],
        "b": q["options"][1],
        "c": q["options"][2],
        "d": q["options"][3]
    }

    while True:
        # show answer choices
        for letter in choices:
            print(letter + ")", choices[letter])

        answer = input("Your answer: ").lower()

        # 50/50 feature
        if answer == "50":
            if used_fifty:
                print("You already used 50/50.\n")
            else:
                used_fifty = True
                correct = q["answer"]

                # remove first two wrong answers found
                removed = 0
                new_choices = {}

                for letter in choices:
                    if letter == correct:
                        new_choices[letter] = choices[letter]
                    elif removed < 2:
                        removed += 1
                    else:
                        new_choices[letter] = choices[letter]

                choices = new_choices
                print("50/50 used! Two wrong answers removed.\n")
            continue

        # check valid input
        if answer in choices:
            break
        else:
            print("Invalid input. Please enter a valid letter.\n")

    # check correct or incorrect
    if answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        correct_letter = q["answer"]
        print("Incorrect.")
        print("Correct answer was", correct_letter + ")", q["options"][ord(correct_letter) - 97])
        print()

# final score
print("Quiz finished!")
print("Your final score is", score, "out of 5. Good job, " + name + "!\n")

# save score history to file
with open("scores.txt", "a") as file:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{time} - {name}: {score}/5\n")

print("Your score has been saved to scores.txt")
