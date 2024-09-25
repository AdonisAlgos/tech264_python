# Get user's input on the same line
name = input('Enter your name: ')
age = input('Enter your age: ')
dob = input('Enter your date of birth (DD/MM/YYYY): ')

# Print "Hi" and user details on the same line
print(f'Hi {name}, you are {age} years old and your DOB is {dob}.')

# Mix the name, age and DOB into one list user_details_list
user_details_list = [name, age, dob]

# Print the user's name, age and DOB from the list
print(f'Name: {user_details_list[0]}, Age: {user_details_list[1]}, Date of Birth: {user_details_list[2]}')

# Check the age is saved as an integer in the list.
# If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))
user_details_list[1] = int(user_details_list[1])
print(type(user_details_list[1]))

# Ask the user for their height in cm and save it to the variable height
height = input('Enter your height in (cm): ')

# Save height as a float in the list, and print the height from the list.
user_details_list.append(float(height))
print(user_details_list[-1])