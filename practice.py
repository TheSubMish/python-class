class Person:
    def __init__(self, name, age):
        """"I am being used every time class is called"""
        self.name = name
        self.age = age
p1 = Person()
print(p1)
        