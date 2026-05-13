# FitFusion – Personalized Fitness Web Application

## Project Description

FitFusion is a personalized fitness web application developed using Python and Flask for the ITM352 final capstone project. The goal of this project is to help users generate workout plans that match their fitness goals, body types, fitness levels, and target areas instead of giving every user the same generic workout routine.

The application allows users to create personalized workout plans, track workout progress, log fitness history, calculate BMI, match with trainers, view leaderboards, and manage their own fitness profile.

This project demonstrates the use of Flask web development, file I/O, data processing, conditional logic, user sessions, CSV and JSON storage, error handling, and UI design.

---

# Features

## Personalized Workout Generator

Users can:

* Choose fitness goals such as:

  * Lose Weight
  * Gain Muscle
  * Build Strength
* Choose body types:

  * Ectomorph
  * Mesomorph
  * Endomorph
* Choose target areas:

  * Arms
  * Legs
  * Stomach
  * Full Body
* Enter fitness level:

  * Beginner
  * Intermediate
  * Advanced

The app then generates a customized workout plan.

---

## User Profile System

Users can:

* Log in using their name
* Access their own profile page
* View only their own workout history
* Track progress over time
* View personal statistics and analytics

---

## Workout Progress Tracking

Users can:

* Log workout date
* Save workout name
* Save weight used
* Save reps completed
* Mark workouts as completed

All progress is stored using CSV file I/O.

---

## Workout Analytics

The app calculates:

* Total workouts
* Completed workouts
* Average weight used
* Average reps
* Workout completion percentage
* Workout streaks

---

## Achievement Badge System

Users can unlock badges such as:

* First Workout Logged
* Consistency Starter
* Fitness Builder
* Workout Champion
* High Completion Rate

---

## Trainer Match Feature

Users can:

* Submit trainer requests
* Get matched with a trainer based on:

  * Fitness goal
  * Fitness level

---

## Leaderboard System

The leaderboard ranks users based on workout points.

Users earn:

* 10 points for completed workouts
* 3 points for incomplete workouts

This feature encourages competition and motivation.

---

## Nutrition Tips Page

The app provides:

* Hydration advice
* Protein recommendations
* General fitness nutrition guidance

---

## Admin Dashboard

The admin dashboard displays:

* Total users
* Total workouts logged
* Completion statistics
* Leaderboard overview

---

# Technologies Used

## Backend

* Python
* Flask

## Frontend

* HTML
* CSS

## Data Storage

* CSV files
* JSON files

## Python Libraries

* Flask
* CSV
* JSON
* Dataclasses
* Datetime
* OS

---

# File Structure

```text
Fitness_app/
│
├── app.py
├── fitness_logic.py
├── progress.csv
├── leaderboard.csv
├── trainer_requests.csv
├── profiles.json
├── requirements.txt
├──Readme.md
│
├── templates/
│   ├── index.html
│   ├── plan.html
│   ├── profile.html
│   ├── login.html
│   ├── history.html
│   ├── leaderboard.html
│   ├── trainer.html
│   ├── nutrition.html
│   └── admin.html
│
└── static/
    └── style.css
```

---

# How to Run the Application

## Step 1 – Install Dependencies

Open terminal and run:

```bash
pip3 install flask
```

---

## Step 2 – Run the Flask Application

```bash
python3 app.py
```

---

## Step 3 – Open the Website

Open your browser and go to:

```text
http://127.0.0.1:5000
```

---

# Testing Plan

The application was tested using:

## Input Validation Testing

* Empty fields
* Invalid numbers
* Negative numbers
* Incorrect text input

## Workout Generation Testing

* Different goals
* Different body types
* Different target areas
* Different fitness levels

## User Profile Testing

* Multiple users logging in
* Correct workout history filtering
* Session tracking

## Progress Tracking Testing

* Saving multiple workout logs
* Verifying CSV file storage
* Testing leaderboard updates

## Error Handling Testing

* Missing form inputs
* Invalid weight/reps
* Missing CSV files

---

# AI Usage

AI was used throughout this project to assist with:

* Flask route structure
* HTML/CSS UI design improvements
* Debugging import and route errors
* Developing workout recommendation logic
* Creating leaderboard logic
* Building user profile session logic
* Improving code organization and readability
* Generating testing ideas and documentation

The AI-generated code was reviewed, modified, tested, and integrated into the application manually. Significant debugging and restructuring were required to adapt the generated outputs into a working Flask application.

---

# Future Improvements

Possible future upgrades include:

* Real password authentication
* Database integration using SQLite
* Real trainer messaging system
* Profile picture uploads
* Workout charts and graphs
* Mobile app version
* Meal planner system

---

# Authors

Developed for ITM352 Final Capstone Project.

Team Members: Thanh Phuong Duong, Nazca Taniguchi, Jordyn


---
# Summary: 

FitFusion demonstrates how Python and Flask can be used to create a realistic MIS-style fitness platform with personalized recommendations, user accounts, data tracking, and analytics. The project combines web development, file management, conditional logic, user interaction, and modern UI design into a complete fitness management application.
