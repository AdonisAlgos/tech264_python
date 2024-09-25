# Learning Python

## Task: Python variable basics
(Ref: variables_examples.py)

### What is a variable?
A variable is a named storage location in a program that holds a value, which can be used and manipulated throughout 
the code. The value stored in a variable can be of different types (like numbers, text, or objects) and can change as 
the program runs.

### Why is it called a variable?
It's called a "variable" because its value can vary or change during the execution of the program. 
The name reflects its purpose: to hold data that can be updated, reused, or manipulated as needed.

### How is using '==' different when assigning variables?
When assigning variables, the = operator is used, not ==. Here's the difference:

**= (Assignment operator):**
Assigns a value to a variable. For example, x = 5 means the value 5 is assigned to the variable x.

**== (Equality operator):**
Compares two values to check if they are equal. For example, x == 5 checks if the value of x is equal to 5.

### Difference between dynamically typed and strongly typed languages
**Dynamically typed language (like Python):** 
The type of a variable is determined at runtime, meaning you don’t need to 
explicitly declare the type. Variables can change types during execution.

**Strongly typed language:**
Variables have a fixed type, and you can't mix types freely. You must explicitly convert 
between types when needed.

#### Example:

```Python
# Python
x = 5   # x is an integer
x = "Hello"  # Now x is a string
```
```
# Java
int x = 5;   # x is an integer
x = "Hello"; # Error! Can't assign a string to an integer
```
### Why does the 'id' of the variable change? 
The id() of a variable in Python represents its memory address. When you overwrite a variable with a new number, 
Python creates a new object in memory for the new value, and the variable points to this new object. That's why the id 
changes—because the variable is now referencing a different object in memory.

Python uses this approach because numbers (and other immutable types) cannot be changed in place. Instead, new objects 
are created when their value is updated.

## Task: Understand operators
(Ref: operators_examples.py)

### What is the difference between an operator and operand?

**Operator:**
A symbol that performs an action or operation on values, like +, -, *, or ==.

**Operand:**
The values or variables on which the operator acts.

## Task: Understand datatypes: int, float, boolean

### Explain and demonstrate: Numeric data types: int and float

**int (integer):** 
Whole numbers without a decimal point.
```Python
x = 5
print(type(x))  # Output: <class 'int'>
```

### Explain and demonstrate: Boolean data type

**float:**
Numbers with a decimal point (fractional part).

```Python
y = 5.0
print(type(y))  # Output: <class 'float'>
```

### Explain why the result is not 0.999999999... with this code and what lesson we should learn:

Floating-point arithmetic is subject to precision limits, and you should be cautious when comparing or working with 
floating-point numbers in critical calculations, as small rounding errors can occur.

## Task: Find out what happens when you convert a string to a boolean
(Ref: boolean_strings_examples.py)

### When does a string convert to False?

A string converts to **False** when it is an empty string "".

### When does a string convert to True?

A string converts to **True** when it is any non-empty string.

## Task: Understanding 'None' in Python
(Ref: none_examples.py)

### What is None in Python?

None is a special constant in Python representing the absence of a value or a null value.

### When is it commonly used?

It is commonly used to indicate missing or uninitialized values, default return values for functions that don't explicitly return anything, or as placeholders.

### Equivalent in other programming languages:

null in JavaScript, Java, C#, or nil in Ruby and Swift.

### What happens when you convert None to a boolean?

None converts to False when evaluated as a boolean.

```Python
# Convert None to boolean
print(bool(None))  # False
```

### Write a piece of Python code to: assign x to be None and print whether my variable x is equal to None.

```Python
# 1. Assign x to None
x = None

# 2. Print whether x is equal to None
print(x is None)  # True
```

## Task: Boolean methods for strings
(Ref: boolean_methods_examples.py)

### Find out what is needed using the comments as a guide. Each of the methods used below should return a boolean (True or False only).

You are not allowed to use any 'if' statements.

```Python
hi = "Hello World!"

# Check if 'hi' is made up of letters only
print(hi.isalpha())  # False because of the space and punctuation

# Check if 'hi' is made up only of lowercase letters
print(hi.islower())  # False because there are uppercase letters

# Check if 'hi' is made up only of uppercase letters
print(hi.isupper())  # False because there are lowercase letters

# Check if 'hi' ends with an exclamation mark
print(hi.endswith('!'))  # True

# Check if 'hi' starts with a capital "H"
print(hi.startswith('H'))  # True
```

## Task: Slice strings

### What is slicing strings?

**Slicing** strings is a method used to extract a portion of a string by specifying a range of indices. The syntax for 
slicing is `string[start:end:step]` where:

* start: the starting index (inclusive),
* end: the ending index (exclusive),
* step: the interval between indices (default is 1).

Code Example: 
```Python
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
```

## Task: Use string methods

### Trim spaces off the beginning and end of a string.

```Python
str_with_extra_spaces = "   extra spaces at the start and end   "

# Prints the length of the string, including the spaces
print(len(str_with_extra_spaces)) 

# Prints the length of the string after trimming spaces from both ends
print(len(str_with_extra_spaces.strip()))
```
[string_methods_examples.py](variables%2Fstring_methods_examples.py)

Methods Explanation:

* **len(str)** gives the length of the string.
* **str.strip()** removes any leading and trailing spaces.

 Write code to do what the comments ask for.

```Python
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
```
[string_methods_examples.py](variables%2Fstring_methods_examples.py)

Methods Explanation:

* **str.count('text')** Counts how many times the substring 'text' appears.
* **str.lower()** Converts all characters in the string to lowercase.
* **str.upper()** Converts all characters in the string to uppercase.
* **str.capitalize()** Capitalizes the first letter of the string.
* **str.replace('with', ',')** Replaces the word 'with' with a comma ,.

## Task: Concatenate these variables with different data types

### What is Concatenation?
Concatenation is the process of joining two or more strings together. In Python, you can use the + operator to 
concatenate strings. However, when trying to concatenate non-string types (e.g., integers or floats) with strings, 
Python will raise an error. To fix this, you need to convert the non-string types to strings before concatenating.

The problem:
```Python
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

print(x + y + z)  # This will not work
```
[string_concatination_examples.py](variables%2Fstring_concatination_examples.py)

The print(x + y + z) statement will throw a TypeError because Python does not automatically concatenate different 
data types.

Solution:
```Python
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"

# Convert x and y to strings and concatenate them with z
print(str(x) + str(y) + z)
```
[string_concatination_examples.py](variables%2Fstring_concatination_examples.py)

Methods Explanation:
* **str(string):** Converts a data type (e.g., integers, floats) into a string.

## Task: Use f-strings to format numbers

### Problem & Solution (problems defined in comments)
```Python
pi = 3.14159265359
# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f'Pi to 3 decimal places: {pi:.3f}')

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f'Pi to 5 decimal places: {pi:.5f}')

score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f'You scored {score_as_decimal}')

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f'You scored {score_as_decimal:%}')

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f'You scored {score_as_decimal:.2%}')

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f'You scored {score_as_decimal:.0%}')
```
[string_format_examples.py](variables%2Fstring_format_examples.py)

Method Explanations:
* **f-string** Formatted string literals allow to easily embed expressions inside string literals.
* **round()** Rounds numbers to a specified number of decimal places.

## Task: Convert/cast this string to an int and float

### Problem & Solution (problems defined in comments)

```Python
int_string = "6"

# convert int_string to an integer
int_string = int(int_string)

# after converting, print its data type to the screen
print(type(int_string))

# convert int_string to float
int_string = float(int_string)

# after converting, print its data type to the screen
print(type(int_string))
```
[cast_convert_examples.py](variables%2Fcast_convert_examples.py)

## Task: Working with a list

### Problem & Solution (problems defined in comments) 

```Python
# Creating a list with pre-defined items: eggs, bread, bananas, biscuits, milk
shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk' ]

# Print the list to the screen 
print(shopping_list)

# Print the data type of 'shopping_list'
print(type(shopping_list))

# Print the first item in the list
print(shopping_list[0])

# Print the last item in the list
print(shopping_list[0])

#Change the second item in the list (i.e. 'bread') to 'rice' instead,
# then print the second item to the screen to prove it's been changed 
shopping_list[1] = 'rice'
print(shopping_list[1])

# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='),
# then check the length of the list (which should now have 6 rather than 5)
shopping_list.append('carrots')
print(len(shopping_list))

# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. 
# Use one of the list's methods to add the two items in one go.
shopping_list.extend(['toffee', 'coffee'])

# Print the 'shopping_list' to check 'toffee' and 'coffee' have been added correctly.
print(shopping_list)

# Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.
shopping_list.remove('bananas')
print(shopping_list)

# Remove the last item ('coffee') from 'shopping_list' using the pop method.
# Check it worked by printing 'shopping_list'
shopping_list.pop()
print(shopping_list)
```
[list_method_examples.py](collections%2Flist_method_examples.py)

Method Explanation:
* **list.append(item)** Adds an item to the end of the list.
* **list.extend(iterable)** Adds all the elements from another list to the end of the current list.
* **list.remove(item)** Removes the first occurrence of the specified item from the list.
* **list.pop([index])** Removes and returns the item at the given index. 
If no index is specified, it removes and returns the last item from the list.

## Task: Get name, age and DOB details from a user

### Write a Python script to: 

1. Prompt and get the user's name, age and DOB. 
2. Print the user's name, age and DOB to the screen and see if you can print "Hi " on the same line.
```Python
# Prompt the user and get the input on the same line
name = input('Enter your name: ')
age = input('Enter your age: ')
dob = input('Enter your date of birth (DD/MM/YYYY): ')

# Print "Hi" and user details on the same line
print(f'Hi {name}, you are {age} years old and your DOB is {dob}.')
```
[get_details_from_user.py](mini_projects%2Fget_details_from_user.py)

## Task: Mix all the data about a user into a list

```Python
# Prompt the user and get the input on the same line
name = input('Enter your name: ')
age = input('Enter your age: ')
dob = input('Enter your date of birth (DD/MM/YYYY): ')

# Mix the name, age and DOB into one list user_details_list
user_details_list = [name, age, dob]

# Print the user's name, age and DOB from the list
print(f'Name: {user_details_list[0]}, Age: {user_details_list[1]}, Date of Birth: {user_details_list[2]}')

# Check the age is saved as an integer in the list. 
# If it's not, work out how to convert it to an integer and add the age integer to the list.
print(type(user_details_list[1]))
user_details_list[1] = int(user_details_list[1])

# Ask the user for their height in cm and save it to the variable height
height = input('Enter your height in (cm)')

# Save height as a float in the list, and print the height from the list.
user_details_list.append(float(height))
print(user_details_list[-1])
```
[get_details_from_user.py](mini_projects%2Fget_details_from_user.py)

## Task: Finish the "Stranded on a Desert Island" game

### How are tuples similar to lists? 
Both tuples and lists are used to store collections of items,
and they allow indexing, slicing, and iteration.

### Are tuples immutable and what does this mean? 
Yes, tuples are immutable. This means their elements cannot be changed, 
added, or removed after the tuple is created.

### What other data types are immutable? 
Other immutable data types include strings, integers, floats, and frozensets.

### What is a good use case for tuples? 
Tuples are useful when you need a fixed collection of related items that should not change, such as coordinates.

### What does the following piece of code do? 
```Python
essentials = ("bread", "eggs", "milk") 
print(essentials) 
print(essentials.count("bread"))
```
* `essentials = ("bread", "eggs", "milk")`Creates a tuple called essentials containing the specified items.

* `print(essentials)` Prints the entire tuple `("bread", "eggs", "milk")`.

* `print(essentials.count("bread"))` Counts and prints the number of times "bread" appears in the tuple.

### Practice using tuples.

```Python
# "Stranded on a Desert Island" game 
# Rationale: Practice tuples 
# Type of exercise: Finish the code 

print("You are stranded on a desert island. You can take only THREE items.")

essential_item1 = input("What is an essential item you would take? ") 
essential_item2 = input("What is an essential item you would take? ") 
essential_item3 = input("What is an essential item you would take? ") 

# save the items as a tuple 
essentials_tuple = (essential_item1, essential_item2, essential_item3)  # ADDED CODE 

# print the tuple 
print("Here are your items as a tuple:", essentials_tuple) 
print("") 
print("I lied. You can take one more item.") 

essential_item4 = input("What is one more essential item you would take? ") 

# try to add the 4th item to the tuple 
# if you can't add the 4th item, work out how to save the 4th item to the tuple 

# ADD CODE
essentials_tuple = essentials_tuple + (essential_item4,)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple) 
```
[stranded_on_dessert_island.py](mini_projects%2Fstranded_on_dessert_island.py)

## Task: Working with dictionaries

### Make a dictionary called "student_1" containing the following information: 
* name: susan 
* stream: tech 
* completed_lessons: 4 (should be saved as an integer not a string) 
* completed_lesson_names: value should be list of these 3 items: "variables", "data_types", "set up" 

```Python
student_1 = {
    'name': 'susan',
    'stream': 'tech',
    'completed_lessons': 4,
    'completed_lesson_names': ['variables', 'data_types', 'set up']
}
```
### Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with? 

A dictionary in Python stores data as key-value pairs. Each key must be unique and acts as a label to access the 
associated value. Values can be of any data type, and they are retrieved by referencing their corresponding key.

```Python
student_1 = {
    'name': 'susan',
    'stream': 'tech',
    'completed_lessons': 4,
    'completed_lesson_names': ['variables', 'data_types', 'set up']
}

# Print the dictionary to the screen
print(student_1)

# Print it's data type to the screen to check it's a dictionary
print(type(student_1))

# Print the value for the key-value pair having the key "stream"
print(student_1['stream'])

# Print the value for 'completed_lesson_names' - check you can see the list of 3 items
print(student_1['completed_lesson_names'])

# Print the data type for the value for 'completed_lesson_names' - check it is a list
print(type(student_1['completed_lesson_names']))

# Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
print(student_1['completed_lesson_names'][0])

# Change the value of "completed_lessons" to 3 (an integer not string). Make sure you change was successful
# by printing your dictionary to the screen again.
student_1['completed_lessons'] = 3
print(student_1)

# Delete "data_types" from the list under the key 'completed_lesson_names'
student_1['completed_lesson_names'].pop(1)
print(student_1)

# Use the keys() method on your dictionary to list all the keys
print(student_1.keys())
```
[dictionary_examples.py](collections%2Fdictionary_examples.py)

## Task: Using sets

### Explain 2 main ways that sets are different to lists and tuples 

* Sets are unordered and unindexed: Unlike lists and tuples, sets don't maintain element order and can't be accessed by index.
* Sets only store unique elements: Sets automatically remove duplicates, while lists and tuples can contain duplicates.

```python
# Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {'apple', 'banana', 'cherry'}

# Print the set 'fruits' 
print(fruits)

# Add "orange" to the fruits set using one of the set's methods.
fruits.add('orange')

# Print the set 'fruits' - check it's added 
print(fruits)

# Remove "banana" from the fruits set using one of the set's methods.
fruits.remove('banana')

# Print the set 'fruits' - check it's removed 
print(fruits)

# Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add('apple')

# Print the final fruits set.
print(fruits)

# Print the 2nd item in the set. If there is any problem doing this, explain.
print(fruits[1])
```
[set_examples.py](collections%2Fset_examples.py)

Observations:
* **Adding another "apple"** doesn't change the set because sets only allow unique elements, 
so adding a duplicate "apple" has no effect.
* **Accessing the 2nd item** can't be done directly via index in a set because sets are unordered.

## Task: Using frozen sets

```python
# Create a frozen set named frozen_set containing elements "hello", "world". 
frozen_set = frozenset({'hello', 'world'})

# Try to add "!" to frozen_set. What happens?
frozen_set.add('!')

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# Try to add frozen_set to normal_set. Why does it work? Explain.
normal_set = normal_set.add(frozen_set)

# Prin[dictionary_examples.py](collections%2Fdictionary_examples.py)t normal_set.
print(normal_set)
```
[frozenset_examples.py](collections%2Ffrozenset_examples.py)

Observations:
* You **can't add elements to a frozenset** because it is **immutable**.
* Adding frozen_set to normal_set works **because frozensets are immutable**, 
and **only immutable types can be elements of a set**.

## Task: Waiter helper

```python
# level 1

# Greet the user
print('Hi there!')

# Print a list of starters
print(['hummus', 'bread', 'olives'])

# Take an input for the user for their starter
customer_order_list = []
customer_order_list.append(input('What started would you like? '))

# Print a list of mains
print(['lamb','pizza','fish'])

# Take an input for the user for their main course
customer_order_list.append(input('What would you like for a main? '))

# Print a list of desserts
print(['fruit', 'ice-cream', 'cake'])

# Take an input for the user for their dessert
customer_order_list.append(input('And what would you like as a dessert'))

# Print all of the user's choices
print(f'You have ordered {customer_order_list[0]} as a starter, {customer_order_list[1]} as a main and to finish off, {customer_order_list[2]} as a dessert.')
# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

# level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
```
[waiter_helper.py](mini_projects%2Fwaiter_helper.py)