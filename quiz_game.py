import time
import random
from questions import questions

def start_timer():
    return time.time()

def time_is_up(start_time, limit=10):
    elapsed = time.time() - start_time
    return elapsed >= limit

def display_question(question, start_time):
    print("\n" + question["question"])
    for key, value in question["options"].items():
        print(f"{key}: {value}")
    print(f"(You have {10 - int(time.time() - start_time)} seconds left...)")

def get_user_answer(start_time):
    while True:
        if time_is_up(start_time):
            print("\nTime's up!")
            return None
        user_input = input("\nYour answer (A, B, C, D): ").strip().upper()
        if user_input in ["A", "B", "C", "D"]:
            return user_input
        print("Invalid input. Please choose A, B, C, or D.")

def play_game():
    random.shuffle(questions)  # Randomize the questions
    score = 0
    for question in questions:
        start_time = start_timer()
        display_question(question, start_time)
        answer = get_user_answer(start_time)
        if not answer:
            print("Moving to the next question...")
            continue
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")
    print(f"\nYour final score is {score}/{len(questions)}")
    save_high_score(score)

def save_high_score(score):
    try:
        with open("high_scores.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0

    if score > high_score:
        print("Congratulations! You have the highest score!")
        with open("high_scores.txt", "w") as file:
            file.write(str(score))
    else:
        print(f"The highest score is still {high_score}.")

def replay():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        print("Invalid input. Please type 'yes' or 'no'.")
