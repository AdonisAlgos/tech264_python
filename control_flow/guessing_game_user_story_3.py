# User story 3
# As a user, I don't want my guesses wasted if I enter something accidentally as my guess which are not digits.

# Define/assign number to a variable called magic_number
magic_number = 10
attempt = 1

# Allow the user 5 guesses
while attempt < 6:
    # Ask user for input
    guess = input("Please make a guess: ")

    # Check if the guess is not a number
    if not guess.isdigit():
        print("Invalid input: Please enter a number")
        continue

    # Cast guess to be of Integer type
    guess = int(guess)

    # Check if the user guess matches the magic_number
    if guess == magic_number:
        # Let the user know if the response was correct or not
        print("Congratulations! You've guessed the correct number!")
        break

    # Check if the user guess is higher than the magic_number
    elif guess > magic_number:
        print("Too high! Try a lower number!")

    # Check if the user guess is lower than the magic_number
    elif guess < magic_number:
        print("Too low! Try a higher number!")

    # Increment attempt by 1
    attempt += 1