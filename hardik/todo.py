def add(addTime):
    taskName = input("Enter task: ")
    if taskName:
        todo_dict[addTime].append(taskName)
    else:
        print("Empty task not added.")

def view():
    for x in todo_dict.keys():
        new = todo_dict[x]
        print("\n" + x + " Tasks:")
        for y in range(len(new)):
            print(f"\tTask {y+1} - {new[y]}")

def viewSpecific(x): 
    new = todo_dict[x]  
    print("\n" + x + " Tasks:")
    for y in range(len(new)):
        print(f"\tTask {y+1} - {new[y]}")

def edit(men):
    editTaskNo = int(input("edit task: "))
    assign = todo_dict[men]
    newTask = input("New task: ")
    if newTask:
        assign[editTaskNo-1] = newTask
    else:
        print("Empty task not updated")

def delTask(delTime):
    delTaskNo = int(input("\ndelete task: "))
    assign = todo_dict[delTime]
    assign.pop(delTaskNo-1)

def invalid():
    print("\ninvalid")

todo_dict = {
    "Morning": [],
    "Afternoon": [],
    "Evening": [],
}

while True:
    try:
        opt = int(input("\n*TO-DO-LIST-MENU*\n1.add\n2.view\n3.edit\n4.delete\n5.exit\n\tChoose:"))
        match opt:
            case 1:
                while True:
                    try:
                        opt1 = int(input("\n*ADD TASK IN*\n1.Morning\n2.Afternoon\n3.Evening\n\tChoose:"))
                        match opt1:
                            case 1:
                                add("Morning")
                                break
                            case 2:
                                add("Afternoon")
                                break
                            case 3:
                                add("Evening")
                                break
                            case _:
                                invalid()
                    except ValueError:
                        invalid()

            case 2:
                view()

            case 3:
                try:
                    editTime = int(input("\n*VIEW*\n1.Morning Tasks\n2.Afternoon Tasks\n3.Evening Tasks\n\tChoose: "))
                    match editTime:
                        case 1:
                            viewSpecific("Morning")
                            edit("Morning")
                        case 2:
                            viewSpecific("Afternoon")
                            edit("Afternoon")
                        case 3:
                            viewSpecific("Evening")
                            edit("Evening")
                        case _:
                            invalid()
                except ValueError:
                    invalid()

            case 4:
                try:
                    optDel = int(input("\nDelete from:\n1.Morning\n2.Afternoon\n3.Evening\n\tChoose:"))
                    match optDel:
                        case 1:
                            viewSpecific("Morning")
                            delTask("Morning")
                        case 2:
                            viewSpecific("Afternoon")
                            delTask("Afternoon")
                        case 3:
                            viewSpecific("Evening")
                            delTask("Evening")
                        case _:
                            invalid()
                except ValueError:
                    invalid()

            case 5:
                print("Exit")
                break

            case _:
                invalid()

    except ValueError:
        invalid()
