# data = input("Enter some data: ")


# with open("fifth_class.txt", "a") as file:
#     file.write(f"{data}\n")


# import os


# value = os.path.exists("sixth_class.txt")

# if value:
#     with open("sixth_class.txt", "r") as file:
#         content = file.read()
#         print(f"Content of sixth_class.txt: {content}")

# else:
#     print("sixth_class.txt does not exist, creating it now.")


# print(f"File exists: {value}")


# os.remove("fifth_class.txt")


# list comprehension example

# list_data = [1, 2, 3, 4, 5]

# dict_data = {"name": "John", "age": 30, "city": "New York"}


# dict_value_to_list = dict_data.values()

# print(dict_value_to_list)

# print(type(dict_value_to_list))


# dict_value_to_list = [value for value in dict_data.values()]  # list comprehension

# print(dict_value_to_list)

# dict_value_to_list = []

# for value in dict_data.values():
#     dict_value_to_list.append(value)


# print(dict_value_to_list)


# print("1. add task")
# print("2. remove task")
# print("3. view tasks")
# print("4. exit")


# print("task 1 - buy groceries")
# print("task 2 - clean the house")
# print("task 3 - finish homework")


# remove line from file


def add_task(task) -> None | str | int:
    with open("tasks.txt", "a") as file:
        file.write(f"{task}\n")


task = add_task("buy groceries")


# with open("tasks.txt", "r") as file:
#     tasks = file.readlines()

#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task.strip()}")

#     line_no = 2  # line number to remove
#     if 0 < line_no <= len(tasks):
#         tasks.pop(line_no - 1)

#     with open("tasks.txt", "w") as file:
#         file.writelines(tasks)

#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task.strip()}")



# with open("todo.json", "w") as file:
    
    
    