from flask import Flask, render_template, request, redirect, url_for, session
import json
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "quiz_secret_key"


def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)


def save_score(name, score, total):
    with open("scores.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time} - {name}: {score}/{total}\n")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            return render_template("index.html", error="Please enter your name.")

        questions = load_questions()
        random.shuffle(questions)
        questions = questions[:5]

        for q in questions:
            correct_answer_text = q["options"][["a", "b", "c", "d"].index(q["answer"])]
            random.shuffle(q["options"])
            new_index = q["options"].index(correct_answer_text)
            q["answer"] = ["a", "b", "c", "d"][new_index]

        session["name"] = name
        session["questions"] = questions
        session["current_question"] = 0
        session["score"] = 0
        session["used_fifty"] = False

        return redirect(url_for("quiz"))

    return render_template("index.html", name=session.get("name"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "questions" not in session:
        return redirect(url_for("index"))

    questions = session["questions"]
    current_question = session["current_question"]

    if current_question >= len(questions):
        return redirect(url_for("result"))

    q = questions[current_question]

    choices = {
        "a": q["options"][0],
        "b": q["options"][1],
        "c": q["options"][2],
        "d": q["options"][3]
    }

    if request.method == "POST":
        answer = request.form.get("answer")

        if not answer:
            return render_template(
                "quiz.html",
                question=q,
                choices=choices,
                number=current_question + 1,
                total=len(questions),
                error="Please choose an answer.",
                used_fifty=session["used_fifty"]
            )

        if answer == q["answer"]:
            session["score"] += 1
            feedback = "Correct!"
        else:
            correct_letter = q["answer"]
            correct_text = q["options"][["a", "b", "c", "d"].index(correct_letter)]
            feedback = f"Incorrect. Correct answer: {correct_letter}) {correct_text}"

        session["feedback"] = feedback
        session["current_question"] += 1
        return redirect(url_for("feedback"))

    return render_template(
        "quiz.html",
        question=q,
        choices=choices,
        number=current_question + 1,
        total=len(questions),
        used_fifty=session["used_fifty"]
    )


@app.route("/feedback")
def feedback():
    if "feedback" not in session:
        return redirect(url_for("quiz"))

    return render_template("feedback.html", feedback=session["feedback"])


@app.route("/fifty")
def fifty():
    if "questions" not in session:
        return redirect(url_for("index"))

    if session["used_fifty"]:
        return redirect(url_for("quiz"))

    questions = session["questions"]
    current_question = session["current_question"]

    if current_question >= len(questions):
        return redirect(url_for("result"))

    q = questions[current_question]

    correct_letter = q["answer"]
    all_letters = ["a", "b", "c", "d"]

    wrong_letters = []
    for letter in all_letters:
        if letter != correct_letter:
            wrong_letters.append(letter)

    removed_letters = random.sample(wrong_letters, 2)

    remaining_choices = {}
    for letter in all_letters:
        if letter not in removed_letters:
            remaining_choices[letter] = q["options"][all_letters.index(letter)]

    session["used_fifty"] = True

    return render_template(
        "quiz.html",
        question=q,
        choices=remaining_choices,
        number=current_question + 1,
        total=len(questions),
        used_fifty=True
    )


@app.route("/result")
def result():
    if "name" not in session:
        return redirect(url_for("index"))

    name = session["name"]
    score = session["score"]
    total = len(session["questions"])

    save_score(name, score, total)

    return render_template("result.html", name=name, score=score, total=total)


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)