# Section 1
str_with_extra_spaces = "   extra spaces at the start and end   "

# Prints the length of the string, including the spaces
print(len(str_with_extra_spaces))

# Prints the length of the string after trimming spaces from both ends
print(len(str_with_extra_spaces.strip()))



# Section 2
example_text = "here's some text with some words of text"

# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count('text'))

# convert example_text to lowercase & print it to the screen
print(example_text.lower())

# convert example_text to uppercase & print it to the screen
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,) instead & print it to the screen
print(example_text.replace('with', ','))