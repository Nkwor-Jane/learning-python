# greeting = "Hello, Jane"
# print(greeting)
# _span = 5
# print(_span)
# _8 = "I am eight years old"
# print(_8)
# userName, userAge = "Jane", 5
# print(userName, userAge)
# name = "Alice" + 42
# print(name)
# print('Hello world')
# print('What is your name?')
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of my name is: ')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print('You will be ' + str(int(myAge) + 1) + ' in a year.')
from typing import List

# print('How many eggs do you have?')
# no_of_eggs = input()
# eggs = int(no_of_eggs)
# print(eggs * 10 / 5)
# print(not False)
# print(not True)
# print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
# print('Input your name and password')
# name = input()
# age = str(input())
#
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age <= str(12):
#     print('You are not Alice, kiddo.')
# else:
#     print('You are neither ALice nor a little kid.')
# spam = 0
# while spam < 5:
#     print('Hello, world.')
#     spam = spam + 1
#infinite while loop as along as input is not Jane, it will keep asking for you name
# name = ''
# while name != 'Jane':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')

# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted')

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
#
# age = 17
# if age >= 18:
#     print("You are old enough to vote")
#     print("Have you registeres to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = 2
# if age <= 4:
#     price = 0
# elif age >= 4 and age <= 18:
#     price = 15
# else:
#     price = 10
# print("Your admission cost is $" + str(price) + ".")
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese','french fries']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
"""this 
is 
multiline 4
comment .... YEAH!"""
