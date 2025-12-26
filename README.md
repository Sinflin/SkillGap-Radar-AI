# AI Task Master

AI Task Master is a lightweight task management web application built using Flask.
It uses explainable, rule-based AI logic to help users prioritize tasks, estimate effort,
and manage work efficiently.

The project focuses on transparent decision-making instead of black-box machine
learning models, making it fast, reliable, and easy to understand.

--------------------------------------------------

FEATURES

- Add tasks with deadline and priority
- View all tasks in a simple dashboard
- Mark tasks as completed
- Explainable AI-based task prioritization
- Estimated time required for each task
- Persistent storage using SQLite
- Clean UI using HTML and CSS

--------------------------------------------------

HOW THE AI WORKS

The application uses rule-based logic instead of heavy machine learning.

- Task priority is calculated using:
  - Time remaining until the deadline
  - User-defined priority level (Low, Medium, High)
- Tasks with higher urgency and priority are ranked first
- Time estimation is derived from predefined rules based on priority

This makes the system:
- Fast
- Deterministic
- Fully explainable

--------------------------------------------------

TECH STACK

Backend:
- Python
- Flask

Frontend:
- HTML
- CSS
- Jinja Templates

Database:
- SQLite

Server:
- Flask Development Server
- Gunicorn (for deployment)

--------------------------------------------------

PROJECT STRUCTURE

SkillGap_Radar/
|
|-- app.py
|-- tasks.db
|-- requirements.txt
|-- Procfile
|
|-- templates/
|   |-- index.html
|
|-- static/
    |-- styles.css

--------------------------------------------------

RUNNING THE PROJECT LOCALLY

Step 1: Install dependencies

pip install flask

Step 2: Run the application

python app.py

Step 3: Open in browser

http://127.0.0.1:5000

--------------------------------------------------

DEPLOYMENT NOTES

This is a server-side Flask application and cannot be deployed as a static website.

Static hosting platforms such as:
- GitHub Pages
- Netlify (static hosting)

will NOT work.

Supported deployment platforms:
- Render
- Railway
- Any Python server running Gunicorn

--------------------------------------------------

USE CASES

- Students managing assignments and exams
- Solo developers tracking tasks
- Hackathon demos
- Productivity tools with explainable logic

--------------------------------------------------

FUTURE IMPROVEMENTS

- Daily schedule generation
- Priority score visualization
- Email reminders
- User authentication
- REST API support

--------------------------------------------------

LICENSE

This project is intended for educational and hackathon use.
You are free to modify and extend it.
