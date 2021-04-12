from art import logo
import random

def check_guess(guess, target):
    if guess < target:
        print("Too low.")
        return False
    elif guess > target:
        print("Too high.")
        return False
    else:
        print(f"You got it. The answer was {target}.")
        return True

def guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)
    print(f"Psst, the correct answer is {random_number}.")

    total_tries = 0
    level = input("Choose a difficulty: Type 'easy' or hard': ").lower()

    if level == "easy":
        total_tries = 10
    else:
        total_tries = 5

    guesses_left = total_tries

    while guesses_left != 0:
        print(f"You have {guesses_left} attempts remaining to guess the number.")
        
        user_guess = int(input("Make a guess: "))
        guesses_left -= 1

        correct_guess = check_guess(user_guess, random_number)
        
        if correct_guess:
            break
        elif not correct_guess and guesses_left > 0:
            print("Guess again.")
        else:
            print("You lose")
    

guessing_game()
