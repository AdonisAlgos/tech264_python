# User story 6
# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.

import random

# Define/assign number to a variable called magic_number
magic_number = random.randint(1, 100)
attempt = 1
print("Enter a number between and including 1 and 100!")
# Allow the user 5 guesses
while attempt < 6:
    # Ask user for input
    guess = input("Please make a guess: ")

    # Check if the guess is not a number
    if not guess.isdigit():
        print(f"Invalid input: Attempt {attempt} out of 5. Please enter a number")
        continue

    # Cast guess to be of Integer type
    guess = int(guess)

    if guess != magic_number and attempt == 5:
        print(f"Game over! The correct number was {magic_number}. Better luck next time!")
        break

    # Check if the user guess matches the magic_number
    if guess == magic_number:
        # Let the user know if the response was correct or not
        print(f"Congratulations! You've guessed the correct number on attempt {attempt} out of 5!")
        break

    # Check if the user guess is higher than the magic_number
    elif guess > magic_number:
        print(f"Too high! Try a lower number! Attempt {attempt} out of 5.")

    # Check if the user guess is lower than the magic_number
    elif guess < magic_number:
        print(f"Too low! Try a higher number! Attempt {attempt} out of 5.")

    # Increment attempt by 1
    attempt += 1