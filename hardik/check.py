class person:
    def __init__(self,name,role):
        self.name = name
        self.role = role
        self.taskName = []
        self.remarks = []

    def viewTask(self):
        if self.taskName:
            print("*submitted task*")
            for task in self.taskName:
                print(task)
        else:
            print("*no submitted task*")

class student(person):
    def submitTask(self, taskName):
        self.taskName.append(taskName)

    def viewRemark(self):
        if self.remarks:
            for remark in self.remarks:
                print(f"remarks: {remark}")
        else:
            print("*no remarks yet*")

class teacher(person):

    def addStudent(self):
        role = "student"
        addName = input("\nEnter name: ")
        personObj[addName] = student(addName,role)
        print("*student added*")

    def giveRemark(self,name,remark):
        personObj[name].remarks.append(remark)

    def viewStudentList(self):
        print("*list of students*")
        n = 1
        for key in personObj.keys():
            if personObj[key].role == "student":
                print(f"{n}. {key}")
                n += 1

personObj = {
    "hardik": student("hardik","student"),
    "don": student("don","student"),
    "mainT" : teacher("mainT","teacher")
}


while True:
    try:
        check = int(input("\n*LOGIN AS*\n1.teacher\n2.student\n3.exit\n\tchoose: "))

        match check:
            case 1:
                tName = input("\n*LOGIN*\nusername: ")
                if tName in personObj.keys() and personObj[tName].role == "teacher":

                    while True:
                        opt = int(input("\n*MENU*\n1.check task\n2.add student\n3.view student\n4.exit\n\tchoose:"))
                        match opt:
                            case 1:
                                name = input("\ncheck task submitted by: ")
                                if name in personObj.keys():
                                    personObj[name].viewTask()
                                    remark = input("\n give remarks: ")
                                    personObj[tName].giveRemark(name,remark)
                            case 2:
                                personObj[tName].addStudent()

                            case 3:
                                personObj[tName].viewStudentList()

                            case 4:
                                break
                else:
                    print("\t*invalid username*")

            case 2:
                name = input("\n*LOGIN*\nusername: ")
                if name in personObj.keys() and personObj[name].role == "student":

                    while True:
                        std = int(input("\n*MENU*\n1.add task\n2.view task\n3.view remark\n4.exit\n\tchoose:"))
                        match std:
                            case 1:
                                taskName = input("\ntask to submit: ")
                                personObj[name].submitTask(taskName)

                            case 2:
                                personObj[name].viewTask()

                            case 3:
                                personObj[name].viewTask()

                                personObj[name].viewRemark()        

                            case 4:
                                break   
                else:
                    print("\t*invalid username*")

            case 3:
                print("*exiting*")
                break
            
            case _:
                print("\n\tinvalid")    

    except ValueError:
        print("\n\tinvalid input")  
