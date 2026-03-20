from Higher_lower_game_data import data
from Higher_lower_game_art import logo, vs
import os
import random
import time

def clear_screen():
    """Clear the screen and print the logo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_random_account():
    """Return a random account from the data."""
    return random.choice(data)

def win_or_loss(account_a, account_b, user_guess):
    """Compare the follower counts of two accounts and return whether the user guessed correctly.

    Args:
        account_a (dict): The first account.
        account_b (dict): The second account.
        user_guess (str): The user's guess, either 'a' or 'b'.

    Returns:
        bool: True if the user guessed correctly, False otherwise."""
    return 'a' == user_guess if account_a["follower_count"] >= account_b["follower_count"] else 'b' == user_guess

def get_valid_input(prompt, valid_options):
    """Get a valid input from the user.

    Args:
        prompt (str): The prompt to be displayed to the user.
        valid_options (list[str]): A list of valid options for the user to enter.

    Returns:
        str: The user's valid input.

    Prints an error message if the user enters an invalid option and prompts the user to enter again until a valid option is entered.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

def format_data(account):
    """Format a celebrity's data into a string.

    Args:
        account (dict): A dict containing the celebrity's name, description, and country.

    Returns:
        str: A string containing the celebrity's name, description, and country.
    """
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, {country}"

def display_matchup(account_a, account_b):
    """Print out the matchup between two accounts.

    Args:
        account_a (dict): A dict containing the first celebrity's name, description, and country.
        account_b (dict): A dict containing the second celebrity's name, description, and country.
    """
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

def main():
    """
    Main entry point of the program.

    Clears the screen, prints a welcome message, and selects a random account from the data.
    Then it enters a loop where it compares the follower counts of two accounts and asks the user to guess which account has more followers.
    If the user guesses correctly, it increments the score and prints a message.
    If the user guesses incorrectly, it prints a message and the final score.
    Then it asks the user if they want to play again.
    If the user answers 'n', it prints "See You" and exits the loop.
    If the user answers 'y', it continues to the next loop iteration.
    """
    clear_screen()
    print("Welcome to the Higher Lower Game")
    time.sleep(2)
    B = get_random_account()
    score = 0
    keep_going = True

    while keep_going:
        clear_screen()
        A = B
        B = get_random_account()
        while B == A:
            B = get_random_account()
        print(f"current score: {score}")
        display_matchup(A, B)
        guess = get_valid_input("Who has more followers? Type 'A' or 'B': ", ['a', 'b'])
        if win_or_loss(A, B, guess):
            score += 1
            print(f"You're right!")
            time.sleep(2)
        else:
            clear_screen()
            print("Sorry, that's wrong\n"
                  f"{A['name']} ha {A['follower_count']}M, mentre {B['name']} ha {B['follower_count']}M.\n"
                  f"Final score: {score}")
            score = 0
            if get_valid_input("Play again, (y/n)?: ", ['yes', 'y', 'no', 'n']).startswith('n'):
                print("See You")
                time.sleep(1.5)
                keep_going = False


if __name__ == "__main__":
    main()