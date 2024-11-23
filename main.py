from quiz_game import play_game, replay

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    while True:
        play_game()
        if not replay():
            print("Thank you for playing! Goodbye!")
            break

