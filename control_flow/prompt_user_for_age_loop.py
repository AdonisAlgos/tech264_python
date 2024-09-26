# SET VARIABLE user_prompt TO TRUE
user_prompt = True
age = None
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")

    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
    if age.isdigit() and 0 < int(age) <= 117:
        # SET user_prompt TO FALSE
        user_prompt = False

    # ADD ELSE STATEMENT HERE
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT
        print("Invalid input: Please enter a number between 0 and 118.")

print(f"Your age is {age}")