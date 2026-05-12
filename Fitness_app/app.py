from flask import Flask, render_template, request, redirect, url_for
from fitness_logic import *
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = "fitness_app_secret_key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form.get("name", "").strip()
    goal = request.form.get("goal", "").strip()
    body_type = request.form.get("body_type", "").strip()
    target_area = request.form.get("target_area", "").strip()
    level = request.form.get("level", "").strip()
    height = request.form.get("height", "").strip()
    weight = request.form.get("weight", "").strip()
    notes = request.form.get("notes", "").strip()

    if name == "" or goal == "" or body_type == "" or target_area == "" or level == "" or height == "" or weight == "":
        error = "Please fill out all required fields."
        return render_template("index.html", error=error)

    try:
        height = float(height)
        weight = float(weight)

        if height <= 0 or weight <= 0:
            error = "Height and weight must be positive numbers."
            return render_template("index.html", error=error)

    except ValueError:
        error = "Height and weight must be numbers."
        return render_template("index.html", error=error)

    user = UserProfile(name, goal, body_type, target_area, level, height, weight, notes)
    workout_plan = generate_workout_plan(user)

    return render_template("plan.html", user=user, workout_plan=workout_plan)


@app.route("/log", methods=["GET", "POST"])
def log_progress():
    if request.method == "POST":
        date = request.form.get("date", "").strip()
        workout = request.form.get("workout", "").strip()
        weight = request.form.get("weight", "").strip()
        reps = request.form.get("reps", "").strip()
        completed = request.form.get("completed", "").strip()

        if date == "" or workout == "" or weight == "" or reps == "" or completed == "":
            error = "Please complete every box before saving your progress."
            return render_template("log_progress.html", error=error)

        try:
            weight = float(weight)
            reps = int(reps)

            if weight < 0 or reps < 0:
                error = "Weight and reps cannot be negative."
                return render_template("log_progress.html", error=error)

        except ValueError:
            error = "Weight must be a number and reps must be a whole number."
            return render_template("log_progress.html", error=error)

        name = session.get("username", "Guest")
        save_progress_log(date, workout, weight, reps, completed, name)
        return redirect(url_for("history"))

    return render_template("log_progress.html")


@app.route("/history")
def history():
    logs = read_progress_logs()
    summary = calculate_progress_summary(logs)

    return render_template(
        "history.html",
        logs=logs,
        summary=summary,
        chart_created=False
    )

@app.route("/trainer", methods=["GET", "POST"])
def trainer():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        goal = request.form.get("goal", "").strip()
        level = request.form.get("level", "").strip()
        message = request.form.get("message", "").strip()

        if name == "" or goal == "" or level == "":
            error = "Please fill out name, goal, and level."
            return render_template("trainer.html", error=error)

        trainer_match = match_trainer(goal, level)
        save_trainer_request(name, goal, level, message)

        return render_template("trainer.html", trainer_match=trainer_match)

    return render_template("trainer.html")


@app.route("/leaderboard")
def leaderboard():
    leaders = read_leaderboard()
    return render_template("leaderboard.html", leaders=leaders)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if name == "":
            error = "Please enter your name to log in."
            return render_template("login.html", error=error)

        session["username"] = name
        return redirect(url_for("profile"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]
    all_logs = read_progress_logs()

    user_logs = []

    for log in all_logs:
        if log.get("name", "").lower() == username.lower():
            user_logs.append(log)

    summary = calculate_progress_summary(user_logs)
    completion_percentage = calculate_completion_percentage(user_logs)
    streak = calculate_workout_streak(user_logs)
    badges = get_achievement_badges(user_logs)

    return render_template(
        "profile.html",
        username=username,
        logs=user_logs,
        summary=summary,
        completion_percentage=completion_percentage,
        streak=streak,
        badges=badges
    )

@app.route("/nutrition")
def nutrition():
    tips = get_nutrition_tips()
    return render_template("nutrition.html", tips=tips)


@app.route("/admin")
def admin():
    summary = get_admin_summary()
    leaders = read_leaderboard()

    return render_template(
        "admin.html",
        summary=summary,
        leaders=leaders
    )

if __name__ == "__main__":
    app.run(debug=True, port=5050)