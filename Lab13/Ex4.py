from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simple sample questions
questions = [
    {
        "question": "What does CPU stand for?",
        "choices": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing User"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is commonly used with Flask?",
        "choices": ["Java", "Python", "C++", "HTML"],
        "answer": "Python"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    # start with first question
    return redirect(url_for("quiz", qnum=0, score=0))

@app.route("/quiz/<int:qnum>", methods=["GET", "POST"])
def quiz(qnum):
    score = int(request.args.get("score", 0))

    if qnum >= len(questions):
        return redirect(url_for("result", score=score))

    if request.method == "POST":
        user_answer = request.form.get("answer")
        if user_answer == questions[qnum]["answer"]:
            score += 1
        return redirect(url_for("quiz", qnum=qnum + 1, score=score))

    return render_template("quiz.html", question=questions[qnum], qnum=qnum)

@app.route("/result")
def result():
    score = request.args.get("score", 0)
    total = len(questions)
    return render_template("result.html", score=score, total=total)

if __name__ == "__main__":
    app.run(debug=True)