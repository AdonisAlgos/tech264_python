# Learning Functions

## Group Task: Make functions

### Task 1: Make a function with no argument
Requirements:

* Create a function named print_something that prints a message.
* Call the function to verify it works.

Solution:

```python
def print_something():
    print("Something")

print_something()
```
[function_examples.py](function_examples.py)

### Task 2: Make a function with one argument

Requirements:

* Improve the previous function by accepting a string as an argument.
* The function should print the string passed to it.

Solution:

```python
def print_something(some_string):
    print(some_string)

print_something("Something")
```
[function_examples.py](function_examples.py)

### Task 3: Make a more interesting version of a function that accepts one argument

Requirements:

* Create a function called greet that accepts a name and uses concatenation to print "Hello, my name is <name>."

Solution:

```python
def greet(name):
    print("Hello, my name is " + name + ".")

greet("Susan")
```
[function_examples.py](function_examples.py)

### Task 4: Make a function with 2 arguments that returns a value

Requirements:

* Fix the provided addition function so it returns the correct value.
* Do not print inside the function.

```
def addition(int1, int2):
    int1 + int2

print(addition(2, 2))
```

Solution:

```python
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))
```
[function_examples.py](function_examples.py)

### Task 5: Make a function with default values

Requirements:

* Modify the addition function to have default values for the parameters, both set to 2.
* Call the function with and without arguments.

Solution:
```python
def addition(int1 = 2, int2 = 2):
    return int1 + int2

print(addition())
print(addition(4, 4))
```
[function_examples.py](function_examples.py)

Explanation:

The function now has default values for int1 and int2. If no arguments are passed, 
it returns 4 (the sum of the default values). When passing arguments, the default values are overwritten.

### Task 6: Make a function that accepts any number of arguments

Requirements:

* Create a function called print_every_number that accepts any number of arguments (a tuple of numbers).
* Print the type of the argument and each number on a new line.

Solution:

```python
def print_every_number(*args):
    print(type(args))
    for element in args:
        print(element)

print_every_number(1, 2, 2, 3, 3, 4, 5, 5)
```
[function_examples.py](function_examples.py)

Explanation:

The *args syntax allows the function to accept any number of arguments. These arguments are treated as a tuple.

### Task 7: Make a function which gives a hint about an argument's data type

Requirements:

* Add type hinting to the greet function to specify that the argument must be a string.

Solution:

```python
def greet(name: str):
    print("Hello, my name is " + name + ".")

greet("Susan")
```
[function_examples.py](function_examples.py)

Explanation:

By adding **: str** after the name argument, we indicate that the greet function expects a string.

### Task 8: Make a function which gives a hint about a return value's data type

Requirements:

* Create a function called division that divides two integers, with default values of 2 and 5.
* Add type hints for both arguments and the return value, specifying that the return type is a float.

Solution:
```python
def divide(num1: int = 2, num2: int = 5) -> float:
    return num1 / num2

a: int = 4
b: int = 6

print(divide(a, b))
print(divide())
```
[function_examples.py](function_examples.py)
### Task 9: What are some good practices when it comes to functions?

* **Single Responsibility:** Each function should perform one clear task.
* **Descriptive Naming:** Use meaningful names that convey the function's purpose.
* **Keep Functions Small:** Aim for concise, focused functions that are easy to read and maintain.
* **Testability:** Ensure functions can be easily tested in isolation.

## Task: Mini calculator using functions

MVP Requirements (each of these should be in a separate function): 

* Can add 2 numbers 
* Can subtract 2 numbers 
* Can multiply 2 numbers 
* Can divide 2 numbers 

Taking it to the next level: 

* Implement more complex operations, such as handling parentheses, exponentiation.
* More advanced operations should continue to be broken into separate functions.

Solution:

```python
# Defining addition
def add(num1, num2):
    return num1 + num2

print(add(5, 3))

# Defining subtraction
def subtract(num1, num2):
    return num1 - num2

print(subtract(10, 4))

# Defining multiplication
def multiply(num1, num2):
    return num1 * num2

print(multiply(6, 7))

# Defining division
def divide(num1, num2):
    return num1 / num2

print(divide(15, 3))

# Defining exponentiation
def exponentiation(num, exponent):
    return num ** exponent

print(exponentiation(2, 3))

# Defining expression handler
def evaluate_expression(expression):
    # eval() handles expressions like (2+3)*4 or 2**3
    return eval(expression)

print(evaluate_expression("(2 + 3) * 4"))
print(evaluate_expression("2 ** 3"))
```
[calculator.py](calculator.py)

