# from common_func import add_numbers as add

# a,b= 5, 10

# def func(a,b):
#     if a == b:
#         print(f"{a} is equal to {b}")
#     elif a < b:
#         print(f"{b} is greater than {a}")
#     else:
#         print(f"{a} is greater than {b}")

#     print(f"value of a is: {a}, value of b is: {b}".format(a=a, b=b))

#     new_var = f"if a == b: {a * b}"
#     print(new_var)


# func(a,b)

# result = add(a, b)
# print(result)


# import random


# num = random.randint(1, 100)

# print(f"Random number generated: {num}")


# import math

# sqrt_num = math.sqrt(num)

# print(type(sqrt_num))

# print(f"Square root of {num} is: {round(sqrt_num,2)}")


# import qrcode

# user_data = input("Enter data to encode in QR code: ")


# img = qrcode.make(user_data)
# type(img)
# img.save("some_file.png")


# user_name = input("Enter your name: ")

# data = user_name.split(".")

# if data[-1] != "png":
#     print("Please enter a valid file name ending with .png")


# try:
#     print(data[1])
# # except IndexError:
# #     print("IndexError: Please ensure you have entered a valid file name with an extension.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
    
# finally:
#     print("Execution completed, whether an error occurred or not.")
    
    
try:
    with open("requiremen.txt", "r") as file:
        lines = file.readlines()
        file.close()
        print(lines)
        for line in lines:
            print(line.strip())
        

except FileNotFoundError:
    print("FileNotFoundError: The file 'requirements.txt' does not exist.")
    
finally:
    print("Execution completed, whether an error occurred or not.")
    

try:
    with open("requiremen.txt", "w") as file:
        file.write("requests\n")
        file.write("numpy\n")
        file.write("pandas\n")
        file.close()

except FileNotFoundError:
    print("FileNotFoundError: The file 'requirements.txt' does not exist.")
    
    
    
