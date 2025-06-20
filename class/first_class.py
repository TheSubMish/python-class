# print("Hello world from first_class.py")


# data types
# int char float double -  a = "Hello world from first_class.py"

var_1 = 10.10

print(type(var_1))

var_2 = "10.10"

var_3 = "hello world"

print(type(var_3))

print(var_3.capitalize())
print(var_3.upper())


# print(type(var_1))
# print(type(var_2))


# python based datatype
# list, tuple, set, dict


list_1 = [1, 2, 3, 4, 5]

list_2 = [1, 2, 3, 4, 5, "Hello", "World", list]

list_1[0] = 10

# print(list)


# print(list)
# print(list_2)

# dict - key-value pairs

dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming", "coding"],
}

# print(dict["hobbies"])


# tuple
_tuple = (1, 2, 3, 4, 5, 10)

# tuple[0] = 10  # This will raise an error because tuples are immutable

# set


_set = {1, 2, 3, 4, 5}


set_1 = {1, 2, 3, 1, 3}


# print(set_1)

# print(type(set_1))
# type conversion

new_list = list(set_1)

# print(new_list)
# print(type(new_list))


new_tuple_list = list(_tuple)

# print(new_tuple_list)
# print(type(new_tuple_list))


new_tuple_list[0] = 10
# print(new_tuple_list)

_tuple = tuple(new_tuple_list)
# print(_tuple)

# print(new_tuple_list.count(10))

# new_tuple_list.append(100)

# print(new_tuple_list)


tuple([1, 2, 3, 4, 5])
 