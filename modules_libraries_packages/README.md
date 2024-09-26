# Learning Modules, Libraries and Packages

* **Library:** A collection of pre-written code (functions, classes, etc.) - collection of modules.
* **Module:** A single Python file containing code (functions, variables, classes).
* **Package:** is just a way to organize code into a folder with multiple files.

## Task: Re-factor your calculator to use a math_operations module.

* Modify your calculator script so that all arithmetic functions are moved to the python file math_operations.py
* In your main calculator script, import math_operations so that the functions are accessed in math_operations.py
* In your main calculator script, modify the calling of the functions so they use the math_operations module

Solution:
```python
# Defining addition
def add(num1, num2):
    return num1 + num2

# Defining subtraction
def subtract(num1, num2):
    return num1 - num2

# Defining multiplication
def multiply(num1, num2):
    return num1 * num2

# Defining division
def divide(num1, num2):
    return num1 / num2

# Defining exponentiation
def exponentiation(num, exponent):
    return num ** exponent

# Defining expression handler
def evaluate_expression(expression):
    # eval() handles expressions like (2+3)*4 or 2**3
    return eval(expression)
```
[math_operations.py](math_operations.py)

```python
from modules_libraries_packages.math_operations import *

print(add(5, 3))
print(subtract(10, 4))
print(multiply(6, 7))
print(divide(15, 3))
print(exponentiation(2, 3))
print(evaluate_expression("(2 + 3) * 4"))
print(evaluate_expression("2 ** 3"))
```
[calculator.py](..%2Ffunctions%2Fcalculator.py)

