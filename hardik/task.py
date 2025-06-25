def view():
    with open("task.txt") as t:
        global read
        read= t.readlines()
    print("VIEWING ALL TASKS:")
    for i in range(len(read)):
        print(f"\tTask {i+1} - {read[i]}")

while True:
    operation = int(input("\nOPTOINS:\n1.ADD TASK\n2.VIEW TASKS\n3.DELETE TASK\n4.EXIT\n\tCHOOSE:"))
    match operation:
        case 1:
            taskName = input("Enter a task:") 
            with open("task.txt","a") as t:
                t.write(f"{taskName}\n")

        case 2:
            view()

        case 3:
            view()
            i = int(input("DELETE TASK: "))
            with open("task.txt","w") as t:
                for final in read:
                    if final != read[i-1]:
                        t.write(final)
      
        case 4:
            print("EXITING")
            break

        case _:
            print("Invalid Input")
