from datetime import datetime, timedelta
# def time():
#     date_line = 7
#     today = datetime.now()
    
#     ask = input("Print out due date, yes/no? ")
#     if ask == "yes":
#         due_date = today + timedelta(days=date_line)
#         remaining_days = due_date - today
#     user_data = today + timedelta(ask)
#     print(user_data)
# # time()

def print_remaining_days(due_date):

    ask = input("Print out due date, yes/no? ")
    if ask == "yes":
        today = datetime.now()
        remaining_days = due_date - today

        return remaining_days

    else:
        return None 


# duedate = datetime(2025,7,24)

# remaining_days = print_remaining_days(duedate)

# if remaining_days:
#     print(remaining_days)
class user:
    def __init__(self, name):
        self.name = name
    # def gretting(self):
    #     return f"Good morning {self.name}"    
                                                                               



task_mrng = []       
task_afternoon = []
task_evng = []
samay = {"morning": [], "afternoon" : [], "evening" : [] }

while True:
    n = 1
    ask = input("Choose the number between \n1.Add \n2.View tasks \n3.Remove tasks \n4.Exit\n")
    match ask:
        case "1":
            when = int(input("When do you want to add your task? \n1. Morning \n2. Afternoon \n3.Evening \n" ))
            match when:
                case 1:
                    task = input("Add tasks: \n")
                    due_days = int(input("Enter due days"))
                    samay["morning"].append({
                        "task": task,
                        "created time": datetime.now(),
                        "due_date": datetime.now() + timedelta(days=due_days)
                    }) + user(task_mrng)
                case 2:
                    samay["afternoon"].append(input("Add tasks:\n"))
                case 3:
                    samay["evening"].append(input("Add tasks:\n"))   
                case _:
                    print("Invalid Input")                 
        case "2":
            which = int(input("Which one do you want to view 1.Morning \n2.Afternoon \n3.Evening \n4.All?\n "))
            match which:
                case 1:
                    print("----Morning Plan----")
                    for i in samay["morning"]:
                        print(f"{n+1}. {i}")
                        n += 1
                case 2:
                    print("----Afternoon Plan----")
                    for i in samay["afternoon"]:
                        print(f"{n+1}. {i}")
                        n += 1
                case 3 :
                    print("----Evening Plan----")
                    for i in samay["evening"]:
                        print(f"{n+1}. {i}")
                        n += 1                
                case 4:
                    for i in samay:
                        for j in samay[i]:
                            print(f"task {n} - {j}")
                            n+=1
                            # j += remaining_days
                case _:
                    print("Invalid Input")            
        case "3":
            choose = int(input("Which task u want to remove?"))
            for i in samay:
                for j in samay[i]:
                    if n == choose:
                        samay[i].remove(j)
                    n+=1
        case "4":
            break      
        case _:
            print("Invalid Input")
            print("Choose the number between 1 to 4")



# from datetime import datetime , timedelta , time ,date
# # import date
# now =  datetime.now()
# print(now)
# today = date.today()
# print(today)
# date.