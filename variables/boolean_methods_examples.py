hi = "Hello World!"

# Check if 'hi' is made up of letters only
print(f'Letters only? {hi.isalpha()}')  # False because of the space and punctuation

# Check if 'hi' is made up only of lowercase letters
print(f'Lowercase letters only? {hi.islower()}')  # False because there are uppercase letters

# Check if 'hi' is made up only of uppercase letters
print(f'Uppercase letters only? {hi.isupper()}')  # False because there are lowercase letters

# Check if 'hi' ends with an exclamation mark
print(f'Ends with exclamation mark? {hi.endswith('!')}')  # True

# Check if 'hi' starts with a capital "H"
print(f'Starts with capital "H"? {hi.startswith('H')}')  # True