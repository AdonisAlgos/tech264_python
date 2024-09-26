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