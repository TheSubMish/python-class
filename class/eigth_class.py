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

