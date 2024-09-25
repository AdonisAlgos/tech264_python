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
