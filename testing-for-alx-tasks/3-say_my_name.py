def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


print(say_my_name("John", "Smith"))
print(say_my_name("Walter", "White"))
print(say_my_name("Bob"))
print(say_my_name("Bob", "4"))
# print(say_my_name("Bob", "Dylan", "White"))
print(say_my_name(4, 5))

try:
    print(say_my_name(12, "White"))
except Exception as e:
    print(e)