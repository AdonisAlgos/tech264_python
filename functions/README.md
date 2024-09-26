# Learning Functions

## Task 1: Make a function with no argument
Requirements:

* Create a function named print_something that prints a message.
* Call the function to verify it works.

Solution:

```python
def print_something():
    print("Something")

print_something()
```

## Task 2: Make a function with one argument

Requirements:

* Improve the previous function by accepting a string as an argument.
* The function should print the string passed to it.

Solution:

```python
def print_something(some_string):
    print(some_string)

print_something("Something")
```

# Task 3: Make a more interesting version of a function that accepts one argument

Requirements:

* Create a function called greet that accepts a name and uses concatenation to print "Hello, my name is <name>."

Solution:

```python
def greet(name):
    print("Hello, my name is " + name + ".")

greet("Susan")
```

## Task 4: Make a function with 2 arguments that returns a value

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

## Task 5: Make a function with default values

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

Explanation:

The function now has default values for int1 and int2. If no arguments are passed, 
it returns 4 (the sum of the default values). When passing arguments, the default values are overwritten.

## Task 6: Make a function that accepts any number of arguments

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

Explanation:

The *args syntax allows the function to accept any number of arguments. These arguments are treated as a tuple.

## Task 7: Make a function which gives a hint about an argument's data type

Requirements:

* Add type hinting to the greet function to specify that the argument must be a string.

Solution:

```python
def greet(name: str):
    print("Hello, my name is " + name + ".")

greet("Susan")
```
Explanation:

By adding **: str** after the name argument, we indicate that the greet function expects a string.

## Task 8: Make a function which gives a hint about a return value's data type

Requirements:

* Create a function called division that divides two integers, with default values of 2 and 5.
* Add type hints for both arguments and the return value, specifying that the return type is a float.

Solution:
```python
def division(num1: int = 2, num2: int = 5) -> float:
    return num1 / num2

a = 4
b = 6

print(division(a, b))
print(division())
```
## Task 9: What are some good practices when it comes to functions?

* **Single Responsibility:** Each function should perform one clear task.
* **Descriptive Naming:** Use meaningful names that convey the function's purpose.
* **Keep Functions Small:** Aim for concise, focused functions that are easy to read and maintain.
* **Testability:** Ensure functions can be easily tested in isolation.