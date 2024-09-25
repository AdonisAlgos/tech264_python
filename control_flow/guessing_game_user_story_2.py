# User story 2
# As a user, I want to be able to guess a number and know if I need to go higher or lower.

# Define/assign number to a variable called magic_number
magic_number = 10

# Allow the user 5 guesses
for attempt in range(1, 6):
    # Ask user for input
    guess = input("Please make a guess: ")

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