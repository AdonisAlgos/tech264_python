# Task data structures
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]] 
dict_data = {
            1: {"name": "Bronson", "money": "$0.05"}, 
            2: {"name": "Masha", "money": "$3.66"}, 
            3: {"name": "Roscoe", "money": "$1.14"}
            }

# Task 1 - Looping through a list and multiplying each number by 2
print("Task 1 -------------------------------------------------------")
for num in list_data:
    print(num * 2)

# Task 2 - Looping through a nested list
print("Task 2 -------------------------------------------------------")
for data in embedded_lists:
    print(data)

# Task 3 - Looping through the nested list
print("Task 3 -------------------------------------------------------")
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

# Task 4 - Looping through a dictionary
print("Task 4 -------------------------------------------------------")
for key in dict_data:
    print(key)

# Task 5 - Looping through a dictionary and print its values
print("Task 5 -------------------------------------------------------")
for value in dict_data.values():
    print(value)

# Task 6 - Loop to print the values of the dictionary items inside a dictionary
print("Task 6 -------------------------------------------------------")
for dict_value in dict_data.values():
    for nested_dict_value in dict_value.values():
        print(nested_dict_value)

# Task 7 - Loop to print specific values of the dictionary items inside a dictionary
print("Task 7 -------------------------------------------------------")
for dict_value in dict_data.values():
    print(dict_value["money"])

# Task 8 - Loop through a list with a nested if statement
print("Task 8 -------------------------------------------------------")
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found 3")
    else:
        print("greater than 3")