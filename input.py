# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name + "!")

# height = input("How tall are you in inches? ")
# height = int(height)
#
# if height >= 36:
#     print("You are tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you are a little older.")
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#  print("\nThe number " + str(number) + " is even.")
# else:
#  print("\nThe number " + str(number) + " is odd.")

#VALIDATE INPUT
# while True:
#  print('Enter your age: ')
#  age = input()
#  if age.isdecimal():
#    break
#  print('Please enter a number for you age.')
# while True:
#  print('Select a new password(letters and numbers only):')
#  password = input()
#  if password.isalnum():
#   break
#   print('Passwords can only have letters and numbers')

splitting = 'My name is Jane'.split()
print(splitting)

#PRINT PICINIC ITEMS

def printPicnic(itemsDict, leftWidth, rightWidth):
 print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
 for k, v in itemsDict.items():
  print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4, 'apples': 12, 'cups':4, 'cookies':800}
print(printPicnic(picnicItems, 12, 5))
print(printPicnic(picnicItems, 20, 6))

#IMPORT CLASSES
from classes import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
