# Learning Workflow

## Task: Print movie rating meanings

Instructions:

* The if statement you make below will print the meaning of the movie rating specified at the beginning of the code. 
You should only need to replace the lines in CAPITALS with your own code.

```python
# possible film ratings are "universal", "pg", "12", "12a", "15", "18"
film_rating = "12a"

# use an if statement to check for "universal" rating
if film_rating == "12a":
    print("all age groups can watch this film")

# check if film rating is "pg"
elif film_rating == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")

# check if film rating is "12" or "12a"
elif film_rating == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")

# check if film rating is "15"
elif film_rating == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")

# check if film rating is "18"
elif film_rating == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")

# ELSE STATEMENT
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
```
[movie_ratings.py](movie_ratings.py)

## Task: Working with 'for loops'

Follow the instructions below to create various 'for loops'. 

```python
list_data = [1, 2, 3, 4, 5] 
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }
``` 

1. Loop through a list 

* Under the starting code, write a for loop to print the double of each number in the list 'list_data'.
* It should loop through the numbers in list_data - each item in the list should be called 'num' (for number) 
* Inside the loop, it should print out the double of each number in the list.

Solution:
```python
list_data = [1, 2, 3, 4, 5] 

for num in list_data:
    print(num * 2)
```
[for_loop_examples.py](for_loop_examples.py)
2. Loop through the 'embedded_lists' list 

* Write another for loop to print the items inside of 'embedded_lists'.
* Each item in the list should be called 'data'.

You should end up with this output: 

```
[1, 2, 3] 
[4, 5, 6] 
```
Solution:
```python
embedded_lists = [[1,2,3],[4,5,6]] 

for data in embedded_lists:
    print(data)
```
[for_loop_examples.py](for_loop_examples.py)

3. Loop through the lists embedded inside a list 

* We need to access the data within the lists, so now we need an embedded loop.
* Create another loop inside of the 'embedded_lists' for loop to list the individual items in the lists. 

You should end up with this output:

```
[1, 2, 3] 
1 
2 
3 
[4, 5, 6] 
4 
5 
6 
```

Solution:

```python
embedded_lists = [[1,2,3],[4,5,6]] 

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
```
[for_loop_examples.py](for_loop_examples.py)

4. Loop through a dictionary 

* Write another for loop to loop through the dictionary 'dict_data'.

You should end up with this output:
```
1 
2 
3 
```
Solution:
```python
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }

for key in dict_data:
    print(key)
```
[for_loop_examples.py](for_loop_examples.py)

5. Loop through a dictionary and print its values 

* Write another for loop to loop through the dictionary 'dict_data'.
* Use the dictionary's value() method to print the value for each key in the dictionary.

You should end up with this output:

```
{'name': 'Bronson', 'money': '$0.05'} 
{'name': 'Masha', 'money': '$3.66'} 
{'name': 'Roscoe', 'money': '$1.14'} 
``` 
Solution:
```python
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }

for value in dict_data.values():
    print(value)
```
[for_loop_examples.py](for_loop_examples.py)

6. Loop to print the values of the dictionary items inside a dictionary 

* Copy and paste the last for loop as a starting point for this loop.
* Generate an embedded for loop (a loop within a loop) to extract and print the values within the dictionary of 
each item in the dictionary.

You should end up with this output:

```
Bronson 
$0.05 
Masha 
$3.66 
Roscoe 
$1.14 
```
Solution:
```python
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }

for dict_value in dict_data.values():
    for nested_dict_value in dict_value.values():
        print(nested_dict_value)
```
[for_loop_examples.py](for_loop_examples.py)

7. Loop to print specific values of the dictionary items inside a dictionary 

* Write another for loop to loop through the dictionary 'dict_data' but this time only print out the money values.

You should end up with this output:

``` 
$0.05 
$3.66 
$1.14 
```
Solution:
```python
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }

for dict_value in dict_data.values():
    print(dict_value["money"])
```
[for_loop_examples.py](for_loop_examples.py)

8. Loop through a list with a nested if statement 

* Write another loop to loop through the items in 'list_data'
* include a nested (indented) if statement inside the loop so that when it loops it checks the number/item in list:
  * if the number is less than 3, it prints 'less than 3' 
  * if the number equals 3, it prints 'I found three' 
  * if the number is greater than 3, it prints 'greater than 3' 

You should end up with this output:

``` 
less than 3 
less than 3 
I found three 
greater than 3 
greater than 3 
``` 

Solution:
```python
list_data = [1, 2, 3, 4, 5] 

for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found 3")
    else:
        print("greater than 3")
```
[for_loop_examples.py](for_loop_examples.py)

## Task: Using 'while loops' with an int

* Initialise x with the value of 0 
* Create a while statement so that it loops while x is less than 10 it should: 
  * Print the value of x to the screen in an f-string 
  * Increment (add 1 to x) 

You should end up with this output:

``` 
print x -> 0 
print x -> 1 
print x -> 2 
print x -> 3 
print x -> 4 
print x -> 5 
print x -> 6 
print x -> 7 
print x -> 8 
print x -> 9 
``` 
Solution:
```python
x = 0

while x < 10:
    print(f'x -> {x}')
    x += 1
```
[while_loops.py](while_loops.py)

* Once your code works, find out what happens when you run the code if you comment out the first line which initialises 'x'.

  * Python will raise a NameError when the condition x < 10 is checked because the variable x must be defined 
  before it is used in the while loop.

* Write a brief comment on the line before the code which increments x to explain what would happen if you don't increment x.

  * If x is not incremented, the loop will run infinitely because the condition (x < 10) will always be true


* Copy and paste your working 'while loop' underneath the 'while loop'. Modify the second copy of the 'while loop' 
so that it breaks out of the loop when x equals 4. 

You should end up with this output:

``` 
print x -> 0 
print x -> 1 
print x -> 2 
print x -> 3 
print x -> 4 
``` 
Solution:
```python
x = 0

while x < 10:
    print(f'x -> {x}')
    
    # If x is equal to 4 then break the loop
    if x == 4:
        break
        
    x += 1
```
[while_loops.py](while_loops.py)

## Task: Use 'while loop' to verify user input of age

1. Loop until age is all digits 

Look at this code: 

``` 
# Ask user for their age 
age = input("What is your age? ") 
print(f" Your age is {age}") 
``` 

The problem with this code is that even if the user is 20, they could enter "20" or "twenty".
Let's standardise the input to get the age as digits... 

Starting code - replace comments in CAPITALS with your code: 

```python
# SET VARIABLE user_prompt TO TRUE 
user_prompt = True
age = None
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE 
while user_prompt:
    age = input("What is your age? ") 

    # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS 
    if age.isdigit() and int(age) <= 117:
        # SET user_prompt TO FALSE 
        user_prompt = False

    # ADD ELSE STATEMENT HERE 
    else:
        # TELL USER THE PROBLEM WITH THEIR INPUT 
        print("Invalid input: Please enter a number lower than 118.")

print(f"Your age is {age}")
```
[prompt_user_for_age_loop.py](prompt_user_for_age_loop.py)

2. Also check age is in the correct range 
* The user could say they are 356000 years old if they want. 
* Assuming the oldest person alive today is 117, modify your code to only allow a maximum of 117 as the age. 

Solution:
```python
int(age) <= 117:
```

## Task: Magic number guessing game

### Level 1 

**User story 1:**
* As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not. 

```python
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
```
[guessing_game_level_1.py](guessing_game_user_story_1.py)

### Level 2 

**User story 2:**

* As a user, I want to be able to guess a number and know if I need to go higher or lower.

```python
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
```
[guessing_game_level_2.py](guessing_game_user_story_2.py)

**User story 3:**
* As a user, I don't want my guesses wasted if I enter something accidentally as my guess which are not digits. 

```python
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
```
[guessing_game_level_3.py](guessing_game_user_story_3.py)

**User Story 4:**

* As a user, after each guess, I would like to know how many guesses I have left. 

```python
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
        print(f"Congratulations! You've guessed the correct number on attempt {attempt} out of 5!")
        break

    # Check if the user guess is higher than the magic_number
    elif guess > magic_number:
        print(f"Too high! Try a lower number! Attempt {attempt} out of 5.")
        
    # Check if the user guess is lower than the magic_number
    elif guess < magic_number:
        print(f"Too low! Try a higher number! Attempt {attempt} out of 5.")
    
    # Increment attempt by 1
    attempt += 1
```
[guessing_game_user_story_4.py](guessing_game_user_story_4.py)

### Level 3 

**User Story 5**

* As a user, I would like the magic to be randomly generated each time I play so it is more fun. 
```python
import random

# Define/assign number to a variable called magic_number
magic_number = random.randint(1, 100)
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
        print(f"Congratulations! You've guessed the correct number on attempt {attempt} out of 5!")
        break

    # Check if the user guess is higher than the magic_number
    elif guess > magic_number:
        print(f"Too high! Try a lower number! Attempt {attempt} out of 5.")
        
    # Check if the user guess is lower than the magic_number
    elif guess < magic_number:
        print(f"Too low! Try a higher number! Attempt {attempt} out of 5.")
    
    # Increment attempt by 1
    attempt += 1
```
[guessing_game_user_story_5.py](guessing_game_user_story_5.py)

**User Story 6** 
* As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly 
and I've used up all my tries.

```python
import random

# Define/assign number to a variable called magic_number
magic_number = random.randint(1, 100)
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
    
    if guess != magic_number and attempt == 5:
        print(f"Game over! The correct number was {magic_number}. Better luck next time!")
        break
        
    # Check if the user guess matches the magic_number
    if guess == magic_number:
        # Let the user know if the response was correct or not
        print(f"Congratulations! You've guessed the correct number on attempt {attempt} out of 5!")
        break

    # Check if the user guess is higher than the magic_number
    elif guess > magic_number:
        print(f"Too high! Try a lower number! Attempt {attempt} out of 5.")
        
    # Check if the user guess is lower than the magic_number
    elif guess < magic_number:
        print(f"Too low! Try a higher number! Attempt {attempt} out of 5.")
    
    # Increment attempt by 1
    attempt += 1
``` 
[guessing_game_user_story_6.py](guessing_game_user_story_6.py)

## Task: Fizz Buzz

Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'

Core: 

* Write a program that prints the numbers from 1 to 100. 
* For multiples of three print "Fizz" instead of the number 
* For the multiples of five print "Buzz" instead of the number 
* For numbers which are multiples of both three and five print "FizzBuzz".

Solution:

```python
# Initiating for loop from 1 to and including 100
for num in range(1,101):
  
    # if num is a multiple of 3 and 5 
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    
    # if num is a multiple of 3
    elif num % 3 == 0:
        print("Fizz")
        
    # if num is a multiple of 5
    elif num % 5 == 0:
        print("Buzz")
        
    else:
        print(num)
```
[fizzbuzz.py](fizzbuzz.py)


Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz" 
Refactor using functions.

Solution:

```python
# Defining fizz_buzz function
def fizz_buzz(fizz_num, buzz_num):
    # Initiating for loop from 1 to and including 100
    for num in range(1, 101):

        # if num is a multiple of fizz_num and buzz_num
        if num % fizz_num == 0 and num % buzz_num == 0:
            print("FizzBuzz")

        # if num is a multiple of fizz_num
        elif num % fizz_num == 0:
            print("Fizz")

        # if num is a multiple of buzz_num
        elif num % buzz_num == 0:
            print("Buzz")

        else:
            print(num)
```
[fizzbuzz.py](fizzbuzz.py)

Acceptance Criteria 

* All core task are done 
* Core works with no error 

## Task: Create a Control Flow game

Battle game 

* Make a 2 player battle game using Python.
* Player selects a character/fighter (from 4-6) or gets one assigned to them randomly.
* If Player 2, let them pick the character/fighter they want. If CPU, assign a character/fighter randomly.
* The two Pokemon/fighters/characters need to fight.
* A winner must be declared via some sort of calculation. 

Bonus: Want to play again?

