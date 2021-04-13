from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_guess(guess, answer, turns):
    """
    Checks answer against guess. Returns the number of turns remaining.
    """
    if guess < answer:
        print("Too low.")
        return turns - 1
    elif guess > answer:
        print("Too high.")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}.")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty: Type 'easy' or hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Print welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a random number between 1 and 100
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}.")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    # First check if the guess is equal to the answer as the condition for the while loop. 
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
