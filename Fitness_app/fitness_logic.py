import csv
import os
import json
from dataclasses import dataclass

PROGRESS_FILE = "progress.csv"
PROFILE_FILE = "profiles.json"


@dataclass
class UserProfile:
    name: str
    goal: str
    body_type: str
    target_area: str
    level: str
    height: float
    weight: float
    notes: str


def calculate_bmi(height, weight):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Healthy Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 1), category


def understand_notes(notes):
    notes = notes.lower()

    if "belly" in notes or "stomach" in notes or "waist" in notes:
        return "stomach"

    elif "arm" in notes or "bicep" in notes:
        return "arms"

    elif "leg" in notes or "glute" in notes or "thigh" in notes:
        return "legs"

    elif "full" in notes or "whole body" in notes:
        return "full body"

    return ""


def save_profile(user):
    profiles = []

    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as file:
            try:
                profiles = json.load(file)
            except json.JSONDecodeError:
                profiles = []

    profiles.append(user.__dict__)

    with open(PROFILE_FILE, "w") as file:
        json.dump(profiles, file, indent=4)


def create_weekly_schedule(target):
    return [
        {"day": "Monday", "focus": f"{target.title()} Workout"},
        {"day": "Tuesday", "focus": "Light Cardio"},
        {"day": "Wednesday", "focus": "Upper Body"},
        {"day": "Thursday", "focus": "Recovery / Stretching"},
        {"day": "Friday", "focus": "Lower Body"},
        {"day": "Saturday", "focus": "Full Body"},
        {"day": "Sunday", "focus": "Rest Day"}
    ]


def generate_workout_plan(user):

    smart_area = understand_notes(user.notes)

    if smart_area != "":
        user.target_area = smart_area

    workouts = {

        "lose weight": {

            "stomach": [
                "Mountain Climbers",
                "Plank",
                "Bicycle Crunches",
                "Jumping Jacks"
            ],

            "arms": [
                "Push-ups",
                "Arm Circles",
                "Tricep Dips",
                "Shadow Boxing"
            ],

            "legs": [
                "Squats",
                "Lunges",
                "Jump Squats",
                "Step-ups"
            ],

            "full body": [
                "Burpees",
                "Jump Rope",
                "Push-ups",
                "Squats"
            ]
        },

        "gain muscle": {

            "stomach": [
                "Weighted Crunches",
                "Leg Raises",
                "Russian Twists",
                "Plank Hold"
            ],

            "arms": [
                "Bicep Curls",
                "Shoulder Press",
                "Tricep Extensions",
                "Hammer Curls"
            ],

            "legs": [
                "Squats",
                "Romanian Deadlifts",
                "Leg Press",
                "Calf Raises"
            ],

            "full body": [
                "Deadlifts",
                "Bench Press",
                "Rows",
                "Squats"
            ]
        },

        "strength": {

            "stomach": [
                "Farmer Carry",
                "Dead Bug",
                "Plank Hold",
                "Hanging Knee Raises"
            ],

            "arms": [
                "Push-ups",
                "Rows",
                "Shoulder Press",
                "Hammer Curls"
            ],

            "legs": [
                "Deadlifts",
                "Hip Thrusts",
                "Squats",
                "Lunges"
            ],

            "full body": [
                "Deadlifts",
                "Push-ups",
                "Rows",
                "Squats"
            ]
        }
    }

    goal = user.goal.lower()
    target = user.target_area.lower()
    level = user.level.lower()

    if goal not in workouts:
        goal = "lose weight"

    if target not in workouts[goal]:
        target = "full body"

    if level == "beginner":
        sets = 2
        reps = "8-10 reps"
        difficulty = 4

    elif level == "intermediate":
        sets = 3
        reps = "10-12 reps"
        difficulty = 7

    else:
        sets = 4
        reps = "12-15 reps"
        difficulty = 9

    exercises = workouts[goal][target]

    plan = []

    for exercise in exercises:

        plan.append({
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "rest": "45-60 seconds"
        })

    bmi, bmi_category = calculate_bmi(user.height, user.weight)

    recommendation = (
        f"Your BMI is {bmi}, which is considered {bmi_category}. "
        f"This workout focuses more on your {target}. "
        f"Your workout difficulty score is {difficulty}/10."
    )

    weekly_schedule = create_weekly_schedule(target)

    save_profile(user)

    return {
        "plan": plan,
        "recommendation": recommendation,
        "bmi": bmi,
        "bmi_category": bmi_category,
        "difficulty": difficulty,
        "weekly_schedule": weekly_schedule
    }


def save_progress_log(date, workout, weight, reps, completed, name):

    file_exists = os.path.exists(PROGRESS_FILE)

    with open(PROGRESS_FILE, "a", newline="") as file:

        fieldnames = [
            "name",
            "date",
            "workout",
            "weight",
            "reps",
            "completed"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "date": date,
            "workout": workout,
            "weight": weight,
            "reps": reps,
            "completed": completed
        })
def read_progress_logs():

    logs = []

    if not os.path.exists(PROGRESS_FILE):
        return logs

    with open(PROGRESS_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:
                if "name" not in row:
                    row["name"] = "Guest"

                if (
                    "weight" not in row or
                    "reps" not in row or
                    "completed" not in row
                ):
                    continue

                row["weight"] = float(row["weight"])
                row["reps"] = int(row["reps"])

                logs.append(row)

            except ValueError:
                continue

    return logs


def calculate_progress_summary(logs):

    if len(logs) == 0:

        return {
            "total_workouts": 0,
            "average_weight": 0,
            "average_reps": 0,
            "completed_workouts": 0
        }

    total_weight = 0
    total_reps = 0
    completed_workouts = 0

    for log in logs:

        total_weight += log["weight"]
        total_reps += log["reps"]

        if log["completed"].lower() == "yes":
            completed_workouts += 1

    average_weight = total_weight / len(logs)
    average_reps = total_reps / len(logs)

    return {
        "total_workouts": len(logs),
        "average_weight": round(average_weight, 2),
        "average_reps": round(average_reps, 2),
        "completed_workouts": completed_workouts
    }

TRAINER_FILE = "trainer_requests.csv"
LEADERBOARD_FILE = "leaderboard.csv"


def match_trainer(goal, level):
    trainers = [
        {
            "name": "Coach Maya",
            "specialty": "Weight Loss",
            "level": "beginner",
            "message": "Best for beginners who want simple fat-loss workouts."
        },
        {
            "name": "Coach Daniel",
            "specialty": "Muscle Gain",
            "level": "intermediate",
            "message": "Best for users who want to build muscle and improve form."
        },
        {
            "name": "Coach Jordan",
            "specialty": "Strength Training",
            "level": "advanced",
            "message": "Best for users who want heavier strength-based training."
        }
    ]

    goal = goal.lower()
    level = level.lower()

    if "lose" in goal:
        return trainers[0]
    elif "muscle" in goal:
        return trainers[1]
    elif "strength" in goal:
        return trainers[2]
    else:
        return trainers[0]


def save_trainer_request(name, goal, level, message):
    file_exists = os.path.exists(TRAINER_FILE)

    with open(TRAINER_FILE, "a", newline="") as file:
        fieldnames = ["name", "goal", "level", "message"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "goal": goal,
            "level": level,
            "message": message
        })


def update_leaderboard(name, completed):
    file_exists = os.path.exists(LEADERBOARD_FILE)

    points = 10 if completed.lower() == "yes" else 3

    with open(LEADERBOARD_FILE, "a", newline="") as file:
        fieldnames = ["name", "points"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "name": name,
            "points": points
        })


def read_leaderboard():
    scores = {}

    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                name = row["name"]
                points = int(row["points"])

                if name not in scores:
                    scores[name] = 0

                scores[name] += points

            except:
                continue

    leaderboard = []

    for name in scores:
        leaderboard.append({
            "name": name,
            "points": scores[name]
        })

    leaderboard.sort(key=lambda user: user["points"], reverse=True)

    return leaderboard

from datetime import datetime, timedelta


def calculate_completion_percentage(logs):
    if len(logs) == 0:
        return 0

    completed = 0

    for log in logs:
        if log["completed"].lower() == "yes":
            completed += 1

    return round((completed / len(logs)) * 100, 1)


def calculate_workout_streak(logs):
    if len(logs) == 0:
        return 0

    workout_dates = set()

    for log in logs:
        try:
            date_object = datetime.strptime(log["date"], "%Y-%m-%d").date()
            workout_dates.add(date_object)
        except:
            continue

    if len(workout_dates) == 0:
        return 0

    today = datetime.today().date()
    streak = 0

    while today in workout_dates:
        streak += 1
        today = today - timedelta(days=1)

    return streak


def get_achievement_badges(logs):
    badges = []

    total_workouts = len(logs)
    completed_workouts = 0

    for log in logs:
        if log["completed"].lower() == "yes":
            completed_workouts += 1

    if total_workouts >= 1:
        badges.append("First Workout Logged")

    if completed_workouts >= 3:
        badges.append("Consistency Starter")

    if completed_workouts >= 5:
        badges.append("Fitness Builder")

    if completed_workouts >= 10:
        badges.append("Workout Champion")

    if calculate_completion_percentage(logs) >= 80 and total_workouts >= 3:
        badges.append("High Completion Rate")

    if len(badges) == 0:
        badges.append("No badges yet. Keep going!")

    return badges


def get_admin_summary():
    logs = read_progress_logs()
    leaderboard = read_leaderboard()

    users = set()

    for log in logs:
        users.add(log.get("name", "Guest"))

    return {
        "total_users": len(users),
        "total_workouts": len(logs),
        "completion_percentage": calculate_completion_percentage(logs),
        "leaderboard_count": len(leaderboard)
    }


def get_nutrition_tips():
    return [
        "Drink enough water before and after workouts.",
        "Eat protein after workouts to help muscle recovery.",
        "Try to eat balanced meals with protein, carbs, and vegetables.",
        "Do not skip meals if your goal is to gain muscle.",
        "For weight loss, focus on consistency instead of extreme dieting."
    ]
def create_progress_chart(logs):
    return False