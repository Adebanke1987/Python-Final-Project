from flask import Flask, render_template, request, redirect, url_for
import random
from questions import questions

app = Flask(__name__)
high_score_file = "high_scores.txt"

@app.route("/")
def home():
    random.shuffle(questions)
    return render_template("quiz.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0
    for question in questions:
        user_answer = request.form.get(question["question"])
        if user_answer == question["answer"]:
            score += 1
    
    # Save high score
    try:
        with open(high_score_file, "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0

    if score > high_score:
        with open(high_score_file, "w") as file:
            file.write(str(score))
        high_score_message = "New High Score!"
    else:
        high_score_message = f"The highest score is still {high_score}."

    return render_template("result.html", score=score, total=len(questions), message=high_score_message)

if __name__ == "__main__":
    app.run(debug=True)
