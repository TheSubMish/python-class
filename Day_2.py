# # num_1 = int(input("Enter a number: "))
# # num_2 = int(input("Enter second number: "))
# # if num_1 ==  num_2:
# #     print("Number are equal")
# # elif num_1 > num_2:
# #     print("Num_1 is greater")   
# # elif num_1 < num_2:
# #     print("Num_2 is greater")
# # else:
# #     print("Both are equal")        
# # table = int(input("Enter the number whose table you want: "))
# # range_start = int(input("Enter range you want to start with: "))
# # range_end = int(input("Enter range: "))
# # for i in range(range_start, range_end +1):
# #     print(f"{table} * {i} = {table *i} ")


# # def add(a,b):
# #     print(f"{a} + {b} = {a+b}")
    

# # def sub(a,b):
# #     print(f"{a} - {b} = {a-b}")
    

# # def multiply(a,b):
# #     print(f"{a} * {b} = {a*b}")

# # def division(a,b):
# #     print(f"{a} / {b} = {a/b}")


# # a = int(input("Enter a number: "))
# # b = int(input("Enter second number: "))
# # while True:
# #     ask = input("Which calculation do you want to 'perfrom Add, Sub, Multiply, Division, Exit: ").lower().strip()
# #     if ask in ["add", "sub" , "multiply", "division"]:
# #         match ask:
# #             case "add":
# #                 add(a,b)
# #                 continue
# #             case "sub":
# #                 sub(a,b)
# #                 continue
# #             case "multiply":
# #                 multiply(a,b)
# #                 continue 
# #             case "division":
# #                 division(a,b)
# #                 continue
# #     elif ask == "exit":
# #         exit()
# #     else:
# #         print("Invalid input!!")                     



# # from datetime import datetime

# # now = datetime.now()
# # print("Current Date and Time:", now)
# # print("Year:", now.year)
# # print("Month:", now.month)
# # print("Day:", now.day)


# import qrcode
# generate = input("What do you want to write? ")
# img = qrcode.make(generate)
# img.save("random.png")


a = 4
print(type(a))
print(type(int))