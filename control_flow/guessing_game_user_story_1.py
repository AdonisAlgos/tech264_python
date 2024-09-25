# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# Define/assign number to a variable called magic_number
magic_number = 10

# Allow the user 5 guesses
for attempt in range(1, 6):
    # Ask user for input
    guess = input("Please make a guess: ")

    # Check if the user guess matches the magic_number
    if int(guess) == magic_number:
        # Let the user know if the response was correct or not
        print("Congratulations! You've guessed the correct number!")
        break

    else:
        print("Guess incorrect. Please try again!")