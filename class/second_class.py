var_bool = True


# if (var_bool is True) and (var_bool is False):
#     print("The variable is True")
# elif var_bool is True or var_bool is False:
#     print("The variable is either True or False")
# else:
#     print("The variable is False")


var_1 = 10
var_2 = 20


# if var_1 == 10:
#     print("Both conditions are true")

# elif var_1 > 5:
#     print("the variable is greater than 5")

# elif var_1 >= 5:
#     print("the variable is greater than or equal to 5")

# elif var_1 < 5:
#     print("the variable is less than 5")

# elif var_1 <= 10:
#     print("the variable is less than or equal to 10")


# # get two variables from the user and check which one is greater
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print(f"{a} is greater than {b}")

#     if a == b:
#         print("Both numbers are equal")

# elif a < b:
#     print(f"{b} is greater than {a}")


# print(f"value of a is: {a}, value of b is: {b}",a,b)


# new_var =  f"if a == b: {a*b}"

# print(new_var)


# loops

# for loop

# items = range(1, 11)
# print("Items in the range are:", items)

# for i in range(1, 11):
#     print(f"Value of i is: {i}")


# list_1 = [1, 2, 3, 4, 5]

# result = 0

# for item in list_1:
#     print(f"Item in list is: {item}")
#     result += item


# print(f"Sum of all items in the list is: {result}")


# for i in range(1, 11):
#     print(f"Current value of i is: {i}")
#     for j in range(1, 11):
#         print(f"i: {i}, j: {j}, i*j: {i*j}")


range_end = 10

# for i in range(1, range_end + 1, 2):
#     # range(1,11)
#     print(f"Current value of i is: {i}")
#     for j in range(1, range_end + 1):
#         print(f"i: {i}, j: {j}, i*j: {i*j}")
#     print("-" * 20)  # Separator for clarity


count = 0

# while count < 10:
#     print(f"Current count is: {count}")
#     count += 1


# while True:
#     user_input = input("Enter 'exit' to stop the loop: ")
#     if user_input.lower() == 'exit':
#         pass
#         print("Exiting the loop.")
#     else:
#         print(f"You entered: {user_input}")


# a = 1

# match a:
#     case a if a < 0:
#         print("a is 1")
#     case 2:
#         print("a is 2")
#     case 3:
#         print("a is 3")
#     case _ if a > 5:
#         print("a is greater than 5")


# _ , a= 1, 2


# for _ in range(1, 11):
#     print("This is a placeholder loop that does nothing.")


# def greet(name):
#     """Function to greet a user by name."""
#     print(f"Hello, {name}!")


# name = input("Enter your name: ")
# greet(name)

# greet("Alice")
# greet("Bob")


# args


def add_numbers(*args):
    """Function to add multiple numbers."""
    print(f"Arguments received: {args}")
    print(f"Type of args: {type(args)}")
    total = 0
    for num in args:
        total += num

    if total > 100:
        print("Total exceeds 100")
        return total

    print("Total is within the limit")
    return total


# list_of_numbers = [1, 2, 3, 4, 5]
# add_numbers(1,2,3,4,5)
# result = add_numbers(*list_of_numbers)
# print(f"Sum of numbers: {result}")


# kwargs
# def print_info(**kwargs):
#     """Function to print user information."""
#     print(f"Keyword arguments received: {kwargs}")
#     print(f"Type of kwargs: {type(kwargs)}")

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# def print_info(name, age, city, hobbies):
#     """Function to print user information."""
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")
#     print(f"Hobbies: {', '.join(hobbies)}")


user_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"],
}


# print_info(**user_info)


# def print_info(name,age=10):
#     """Function to print user information with a default age."""
#     print(f"Name: {name}")
#     print(f"Age: {age}")


# print_info("Alice",20)


# ask user for two numbers and ask for what calculation to perform, create functions for addition, subtraction, multiplication, and division using match case return the result of the calculation


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))


# def add(x, y):
#     """Function to add two numbers."""
#     return x + y


# def subtract(x, y):
#     """Function to subtract two numbers."""
#     return x - y


# def multiply(x, y):
#     """Function to multiply two numbers."""
#     return x * y


# def divide(x, y):
#     """Function to divide two numbers."""
#     if y == 0:
#         return "Error: Division by zero"
#     return x / y


# while True:
#     match input("Enter operation (add, subtract, multiply, divide): ").strip().lower():
#         case "add":
#             result = add(a, b)
#         case "subtract":
#             result = subtract(a, b)
#         case "multiply":
#             result = multiply(a, b)
#         case "divide":
#             result = divide(a, b)
#         case "exit":
#             print("Exiting the calculator.")
#             break
#         case _:
#             result = "Invalid operation"
#             break

# print(f"Result of the operation: {result}")
# result = add(a, b)
# print(f"Result of addition: {result}")


# def hello_func(name):
#     # single line comment
#     """
#     Function to print a hello message.
#     """
#     print(f"Hello, {name}")

#     return "Hello from hello_func!"


# txt = hello_func("python")

# print(txt)

# list_parameter = [1, 2, 3, 4, 5]


# # args


def print_list(*args):
    """
    Function to print a list of arguments.
    """
    print("Arguments received:", args)
    for item in args:
        print(item)


# # Calling the function with a list
# print_list(1, 2, 3, 4, 5)

# print_list(*list_parameter)


# # kwargs


def print_dict(**kwargs):
    """
    Function to print a dictionary of keyword arguments.
    """
    print("Keyword arguments received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with a dictionary

dict_data = {
    "name": "Python",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"],
}

# print_dict(
#     name="Alice", age=30, city="New York", hobbies=["reading", "gaming", "coding"]
# )

# print_dict(**dict_data)



import random

def generate_random_number(start, end):
    """
    Function to generate a random number between start and end.
    """
    return random.randint(start, end)


# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# random_number = generate_random_number(start, end)
# print(f"Random number generated between {start} and {end}: {random_number}")


# from django.utils import timezone

# def get_current_datetime():
#     """
#     Function to get the current date and time.
#     """
#     return timezone.now()

# current_datetime = get_current_datetime()
# print("Current date and time:", current_datetime)