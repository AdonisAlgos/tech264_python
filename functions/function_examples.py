print("Task 1 ------------------------------")
def print_something():
    print("Something")

print_something()

print("Task 2 ------------------------------")
def print_something(some_string):
    print(some_string)

print_something("Something")

print("Task 3 ------------------------------")
def greet(name):
    print("Hello, my name is " + name + ".")

greet("Susan")

print("Task 4 ------------------------------")
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2))

print("Task 5 ------------------------------")
def addition(int1 = 2, int2 = 2):
    return int1 + int2

print(addition())
print(addition(4, 4))

print("Task 6 ------------------------------")
def print_every_number(*args):
    print(type(args))
    for element in args:
        print(element)

print_every_number(1, 2, 2, 3, 3, 4, 5, 5)

print("Task 7 ------------------------------")
def greet(name: str):
    print("Hello, my name is " + name + ".")

greet("Susan")

print("Task 8 ------------------------------")
def division(num1: int = 2, num2: int = 5) -> float:
    return num1 / num2

a = 4
b = 6

print(division(a, b))
print(division())