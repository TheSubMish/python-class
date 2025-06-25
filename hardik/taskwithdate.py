from datetime import datetime, timedelta

def view():
    for x in range(len(task)):
        print(f"TASK {x+1} - {task[x]}" + f"\tDUE DATE: {datetime.now() + timedelta(days = dueDays)}")

def invalid():
    print("INVALID INPUT")

task = []
while True:
    try:
        OPT = int(input("\n1.INPUT TASK\n2.VIEW TASK\n3.DELETE TASK\n4.EXIT\n\tCHOOSE:"))
        match OPT:
            case 1:    
                task.append(input("\nENTER A TASK: "))
                while True:
                    try:
                        dueDays = int(input("ENTER DUE DATE:"))
                        break
                    except ValueError:
                        invalid()

            case 2:
                view()

            case 3:
                view()
                try:
                    delTask = int(input("\nDELETE TASK: "))
                    task.pop(delTask-1)
                except ValueError:
                    invalid()

            case 4:
                print("EXITING")
                break

            case _:
                invalid()

    except ValueError:
        invalid()