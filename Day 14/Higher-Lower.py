# Import logo art, data, random and clear modules
from art import logo, vs
from game_data import data
import random
from replit import clear

# Generate second random number different from previous
def get_next_data(random_data_1):
    """
    Returns a random account dictionary from the data list that is not equal to the previous account dictionary.
    """
    random_data_2 = random.choice(data)
    while random_data_2 == random_data_1:
        random_data_2 = random.choice(data)
    return random_data_2

# Compare random data 'followers' to get higher
def compare_followers(followers_1, followers_2):
    """
    Compares the followers for each account holder.
    Returns 'A' or 'B' depending on the higher follower count.
    """
    if followers_1 > followers_2:
        return "A"
    elif followers_1 < followers_2:
        return "B"

# Compare user input to true result
def check_user_choice(user_input, ground_truth):
    """
    Checks the user choice against the ground truth.
    """
    return user_input == ground_truth

# Compute score
def compute_score(correct, score):
    """
    Increments the user score if correct.
    """
    if correct:
        return score + 1
    return score

# Print random data
def display_data(data_dict):
    """
    Returns the account data to be displayed.
    """
    return f"{data_dict['name']}, a {data_dict['description']}, from {data_dict['country']}."

def play_game():
    """
    Starts the higher-lower game.
    """
    # Print welcome message / logo
    print(logo)
    user_score = 0
    # Get random account within data
    person_1 = random.choice(data)

    game_over = False

    while not game_over:
        person_2 = get_next_data(person_1)

        print(f"Compare A: {display_data(person_1)}")

        print(vs)

        print(f"Against B: {display_data(person_2)}")

        # Get result
        result = compare_followers(person_1["follower_count"], person_2["follower_count"])

        # Get user input: A or B
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Calculate user score
        correct = check_user_choice(user_choice, result)
        user_score = compute_score(correct, user_score)

        clear()
        print(logo)

        if correct:
            # Print winning message - continue game
            print(f"You're right! Current score: {user_score}.")
            person_1 = person_2
        else:
            # Print losing message - exit game
            print(f"Sorry, that's wrong. Final score: {user_score}.")
            game_over = True

    #Restart game
    restart_game = input("Do you want to play again? 'Y' or 'N': ").upper()
    if restart_game == "Y":
        clear()
        play_game()


play_game()
