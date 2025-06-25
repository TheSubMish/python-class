class Dummy:

    # name = "default"
    # age = 30

    def __init__(self, name, age=30):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"

    def farewell(self):
        return f"Goodbye, {self.name}!"


# obj1 = Dummy("Alice")
# obj2 = Dummy("Bob")

# data = obj1.greet()
# print(data)

# data = obj2.farewell()
# print(data)


class Person(Dummy):

    def __init__(self, name, age):
        super().__init__(name, age)

    def says(self):
        return f"{self.name} says hello!"


# obj1 = Person("Alice", 25)
# obj2 = Person("Bob", 30)


# data = obj1.greet()
# print(data)

# data = obj2.farewell()
# print(data)


class Student(Person, Dummy):

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying!"

    def get_student_id(self):
        return f"Student ID: {self.student_id}"


obj1 = Student("Alice", 25, "S123")

print(obj1.greet())
print(obj1.get_student_id())
print(obj1.study())
print(obj1.says())
print(obj1.farewell())


class Todo:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task '{task}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task}")


obj1 = Todo()
obj2 = Todo()

users = {
    "user1": obj1,
    "user2": obj2,
}


while True:

    user = input("Enter user (user1/user2): ").strip().lower()
    if user not in users:
        print("Invalid user. Please enter 'user1' or 'user2'.")
        users[user] = Todo()

    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task to add: ")
        users[user].add_task(task)
        print(f"Task '{task}' added.")

    elif choice == "2":
        task = input("Enter the task to remove: ")
        users[user].remove_task(task)

    elif choice == "3":
        users[user].list_tasks()

    elif choice == "4":
        print("Exiting the Todo List.")
        break

    else:
        print("Invalid choice, please try again.")


# obj2 = Todo()

# while True:
#     print("\nTodo List Menu:")
#     print("1. Add Task")
#     print("2. Remove Task")
#     print("3. List Tasks")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         task = input("Enter the task to add: ")
#         obj2.add_task(task)
#         print(f"Task '{task}' added.")

#     elif choice == "2":
#         task = input("Enter the task to remove: ")
#         obj2.remove_task(task)

#     elif choice == "3":
#         obj2.list_tasks()

#     elif choice == "4":
#         print("Exiting the Todo List.")
#         break

#     else:
#         print("Invalid choice, please try again.")
