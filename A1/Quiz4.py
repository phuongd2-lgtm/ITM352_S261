#Quiz 3: Third Version
# Name: Phuong Duong
# Date: Feb 24,2026
# Make a list with the questions and correct answers.
# Make QUESTIONS a dictionary, to include answer options and the correct choice

QUESTIONS = {
    "What is the airspeed of a laden swallow in miles per hour? ": ("12", ["10", "12", "14"]),
    "What is the capital of Texas? ": ("Austin", ["Dallas", "Houston", "Austin", "San Antonio"]),   
    "The Last Super was printed by which artist ": ("da Vinci", ["Michelangelo", "Raphael", "Donatello"]),
}

for question, options in QUESTIONS.items():
    correct_answer = options[0]
    sorted_options = sorted(options)  # The first option is the correct anser
    for label, alternative in enumerate(sorted_options, start=1):
        print(f" {label}. {alternative}")
    
    
    answer_label = int(input(question + ": "))
    answer = sorted_options[answer_label - 1]  
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}' not '{answer}'.")