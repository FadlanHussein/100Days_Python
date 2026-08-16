import os
import json
from flask import Flask, render_template, request

app = Flask(__name__)
FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), "feedback.txt")

def get_all_feedback():
    """Load all feedback from file."""
    if not os.path.exists(FEEDBACK_FILE):
        return []
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_feedback(name, email, message):
    """Save feedback to JSON file."""
    feedback_list = get_all_feedback()
    feedback_list.append({
        "name": name,
        "email": email,
        "message": message
    })
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(feedback_list, file, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        
        save_feedback(name, email, message)
        return render_template("contact.html", success=True)
        
    return render_template("contact.html")

@app.route("/feedback")
def show_feedback():
    data = get_all_feedback()
    return render_template("feedback.html", feedback=data)

if __name__ == "__main__":
    app.run(debug=True)