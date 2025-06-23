
def task():
    taskName = input("TASK NAME: ")
    return taskName

def morningTask():
    print("MORNIG TASKS:")
    global morning
    morning = todo_dict["morning"]
    for x in range(len(morning)):
        print(f"\tTask {x+1} - {morning[x]}")

def eveningTask():
    print("EVENING TASKS:")
    global evening
    evening = todo_dict["evening"]
    for x in range(len(evening)):
        print(f"\tTask {x+1} - {evening[x]}")

def nighttask():
    print("NIGHT TASKS:")
    global night
    night = todo_dict["night"]
    for x in range(len(night)):
        print(f"\tTask {x+1} - {night[x]}")


def delTask():
    return int(input("DELETE TASK: "))

def invalid():
    print("Invalid Input\n")

todo_dict = {
    "morning":[],
    "evening":[],
    "night":[]
}

while True:
    operation = int(input("1.ADD TASK\n2.VIEW TASKS\n3.DELETE TASK\n4.EXIT\n\tCHOOSE:"))

    match operation:
        case 1:
            time = int(input("ADD TASK FOR:\n1.MORNING\n2.EVENING\n3.NIGHT\n\tCHOOSE: "))
            match time:
                case 1:
                    todo_dict["morning"].append(task())
                case 2:
                    todo_dict["evening"].append(task())
                case 3:
                    todo_dict["night"].append(task())
                case _:
                    invalid()

        case 2:
            viewTask = int(input("VIEW TASKS FOR\n1.MORNINIG\n2.EVENING\n3.NIGHT\n4.ALL\n\tCHOOSE:"))

            match viewTask:
                case 1:
                    morningTask()
                case 2:
                    eveningTask()
                case 3:
                    nighttask()
                case 4:
                    morningTask()
                    eveningTask()
                    nighttask()
                case _:
                    invalid()
                    
        case 3:
            i = int(input("DELETE TASK FOR:\n1.MORNINIG\n2.EVENING\n3.NIGHT\n\tCHOOSE: "))
            
            match i:
                case 1:
                    morningTask()
                    morning.pop(delTask()-1)
                case 2:
                    eveningTask()
                    evening.pop(delTask()-1)
                case 3:
                    nighttask()
                    night.pop(delTask()-1)
                case _:
                    invalid()

            
        case 4:
            print("EXITING")
            break

        case _:
            invalid()
