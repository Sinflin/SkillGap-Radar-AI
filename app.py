from flask import Flask, render_template, request, redirect
import sqlite3
import uuid
import datetime

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect("tasks.db")

conn = get_db()
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    name TEXT,
    deadline TEXT,
    priority TEXT,
    status TEXT
)
""")
conn.commit()

# ---------- AI LOGIC ----------
def priority_score(task):
    days_left = (
        datetime.date.fromisoformat(task["deadline"])
        - datetime.date.today()
    ).days
    urgency = max(0, 10 - days_left)
    weight = {"Low": 1, "Medium": 2, "High": 3}[task["priority"]]
    return urgency * weight

def estimate_time(priority):
    return {
        "Low": "30–45 min",
        "Medium": "1–2 hours",
        "High": "2–4 hours"
    }[priority]

# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    c = conn.cursor()

    if request.method == "POST":
        c.execute(
            "INSERT INTO tasks VALUES (?, ?, ?, ?, ?)",
            (
                str(uuid.uuid4()),
                request.form["name"],
                request.form["deadline"],
                request.form["priority"],
                "Pending"
            )
        )
        conn.commit()
        return redirect("/")

    rows = c.execute("SELECT * FROM tasks").fetchall()
    tasks = [{
        "id": r[0],
        "name": r[1],
        "deadline": r[2],
        "priority": r[3],
        "status": r[4]
    } for r in rows]

    return render_template("index.html", tasks=tasks)

@app.route("/done/<task_id>")
def done(task_id):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET status='Done' WHERE id=?",
        (task_id,)
    )
    conn.commit()
    return redirect("/")

@app.route("/healthz")
def healthz():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
