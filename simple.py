# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age


# class Student(Person):
#     def __init__(self,name,age):
#         super().__init__(name=name,age=age)

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, year):
#         if year > 0:
#             self.age = year
#         else:
#             print("Born year must me more than 0")

        
            
# class Teacher(Person):
#     def __init__(self , name,age,salary):
#         super().__init__(name,age)
#         self.__salary = salary

#     @property
#     def salary(self):
#         return self.__salary
    
#     @salary.setter
#     def salary(self, amount):
#         if amount < 10000:
#             self.__salary = amount
#         else:
#             print("Work hard")
# # p1 = Student("Sanjeet", 0)
# # print(p1.__name)
# # print(p1.age)

# # p1.age = 0

# # print(p1.age)
# t1 = Teacher("Hero", 21, 1111)
# t1.salary = 11000
# print(t1.salary)





















