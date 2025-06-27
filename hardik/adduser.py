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

def dataBase():
    users[username] = todo()

def listUser():
    print("*AVAILABLE USERS*")
    x = 1
    for key in users.keys():
        print(x + ".",key)
        x += 1

users = {"admin": todo()}
userData = {"admin": "admin"}

while True:
    try:
        first = int(input("\n*MAIN MENU*\n1.add user\n2.login\n3.list users\n4.exit\n\tCHOOSE: "))

        match first:
            case 1:
                username = input("Enter new username: ")
                passWord = input("Enter new password: ")
                userData[username] = passWord
                dataBase()

            case 2:
                logUsername = input("\n*USER LOGIN*\nusername: ")
                logPassword = input("password: ")
                try:
                    if userData[logUsername] == logPassword:
                        cUser = users[logUsername]

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
                                        print("\n\tINVALID INPUT")
                                            
                            except ValueError:
                                print("\n\tINVALID INPUT")

                except Exception:
                    print("\n\t*INCORRECT username or password*")
            
            case 3:
                listUser()
            
            case 4:
                print("\nEXITING")
                break
            
            case _:
                print("INVALID INPUT")
    
    except ValueError:
        print("\n\t*INVALID INPUT*")