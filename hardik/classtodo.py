class todo:
    def __init__(self):
        self.todoTask = []

    def addTask(self):
        taskName = input("\nEnter task: ")
        if taskName:
            self.todoTask.append(taskName)
            print("\n\t*TASK ADDED*")
        else:
            print("\nEmpty task not added.")
    
    def viewTask(self):
        if self.todoTask:
            print("\n*TASKS*")
            for x in range(len(self.todoTask)):
                print(f"\tTask {x+1} - {self.todoTask[x]}")
        else:
            print("\n*TASK EMPTY*")

    def delTask(self):
        if self.todoTask:
            try:
                x = int(input("\nDELETE TASK: "))
                if 1 <= x <= len(self.todoTask):
                    self.todoTask.pop(x-1)
                    print("\n\t*TASK DELETED*")
                else:
                    print("\n*TASK NOT FOUND*")
            except ValueError:
                print("\n*INVALID INPUT*")
        else:
            print("\n*NO TASKS TO DELETE*")

        
user1 = todo()
user2 = todo()

users = {
    "user1": user1,
    "user2": user2
}

try:
    while True:
        login = (input("\n*USER LOGIN*\n1.user1\n2.user2\n3.exit/x\n\tCHOOSE: ")).lower()

        if login in users:
            cUser = users[login]
        elif login in ["exit","3","x"]: 
            print("\nEXITING")
            break
        else:
            print("\nUSER NOT AVAILABLE")
            continue

        while True:
            try:
                userMenu = int(input("\n*TO-DO-MENU\n1.add\n2.view\n3.delete\n4.exit\n\tCHOOSE: "))
                match userMenu:
                    case 1:
                        cUser.addTask()
                            
                    case 2:
                        cUser.viewTask()

                    case 3:
                        cUser.viewTask()
                        cUser.delTask()

                    case 4:
                        print("\nexiting")
                        break
                     
                    case _:
                        print("\nINVALID INPUT")
                        
            except ValueError:
                print("\nINVALID INPUT")

except ValueError:
                print("\nINVALID INPUT")