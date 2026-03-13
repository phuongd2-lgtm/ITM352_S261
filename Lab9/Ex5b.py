import json

# open the JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# print the contents
for q in questions:
    print("Question:", q["question"])
    print("Options:", q["options"])
    print("Answer:", q["answer"])
    print()