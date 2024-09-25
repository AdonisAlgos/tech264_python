print("Task 1 -----------------------------------------------------------")
# Initiating for loop from 1 to and including 100
for num in range(1, 101):

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

print("Task 2 -----------------------------------------------------------")
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
