



class Todolist:
    def __init__(self):
        # print('-----To do list----')
        self.tasks = []
    def add_tasks(self):
        add_task = input("Enter a tasks: ")
        self.tasks.append(add_task)
    def view_tasks(self):
        print("Tasks are: \n")
        n = 0
        for i in self.tasks:
            print("-----Tasks------")
            print(f"{n+1}. {i}")
            n += 1
    def remove_tasks(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
obj1 = Todolist()
obj2 = Todolist()
obj3 = Todolist()                

users ={
   "user1" : obj1,
   "user2" : obj2,
   "user3" : obj3,
}
while True:
    user = input("Choose the user\n 1. user1\n 2. user2\n 3. user3\n").lower().strip()
    if users.get(user,None):
        print("To do list \n ")
        print("1. Add task\n")
        print("2. view task\n")
        print("3. remove task\n")
    else:
        print("Invalid Users ") 
        continue
    choose = input("Choose the  number between 1 to 3: ")
    if choose == "1": 
        users.get(user).add_tasks()
    elif choose == "2":
        users.get(user).view_tasks()
    elif choose == "3":
        users.get(user).remove_tasks()
    else:
        print("Invalid input")
        continue        
