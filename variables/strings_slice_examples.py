Hw = "Hello world!"
print(Hw)

# Find out how many characters Hw has
print(len(Hw))  # Outputs 12 (length of the string)

# Get the character in the first position in Hw
print(Hw[0])  # Outputs 'H'

# Get the last character
print(Hw[-1])  # Outputs '!'

# Get the 2nd last character
print(Hw[-2])  # Outputs 'd'

# Write a comment to EXPLAIN what does this do
print(Hw[2:])  # Prints from the 3rd character to the end: "llo world!"

# Write a comment to EXPLAIN what does this do
print(Hw[-3:])  # Prints the last 3 characters: "ld!"

# Write a comment to EXPLAIN what does this do
print(Hw[:5])  # Prints the first 5 characters: "Hello"

# Starts from the second, stops at the fifth (doesn't include it)
print(Hw[1:5])  # Outputs "ello"