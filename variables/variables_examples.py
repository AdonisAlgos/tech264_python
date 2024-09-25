# Creating Variables
num = 10
dec = 10.5
name = "Adonis"

# Displaying the type of the variables
print(type(num))
print(type(dec))
print(type(name))

# Displaying the change of variable id when changing variable value
print(id(num))
num = 12
print(id(num))

# Asking for user input and printing the value
user_input = input("Please add your name: ")
print(user_input)