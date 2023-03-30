# def hello(name):
#     print('Howdy!' + name)
# hello('Jane')
#
# def intro(name,language, experience):
#     print(f""" Hi everyone, I am {name}, I work with {language} for my
#     programming. I have {experience} days experience with this {language}
# """)
# intro('Jane', 'Python', 3)
#
# import random
# def getAnswer(answerNumber):
#      if answerNumber == 1:
#         return 'It is certain'
#      elif answerNumber == 2:
#         return 'It is decidedly so'
#      elif answerNumber == 3:
#         return 'Yes'
#      elif answerNumber == 4:
#         return 'Reply hazy try again'
#      elif answerNumber == 5:
#         return 'Ask again later'
#      elif answerNumber == 6:
#         return 'Concentrate and ask again'
#      elif answerNumber == 7:
#         return 'My reply is no'
#      elif answerNumber == 8:
#         return 'Outlook not so good'
#      elif answerNumber == 9:
#         return 'Very doubtful'
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
#
#
# print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice',sep='')
#
# #GLOBAL AND LOCAL scope
# def spam():
#     global eggs
#     eggs = 'spam' #this is global
# def bacon():
#     eggs = 'bacon' #this is local
# def ham():
#     print(eggs) #this is global
# eggs = 42 #this is global
# spam()
# print(eggs)
#
# def spam1(divideBy):
#     try:
#         return  42 /divideBy
#     except ZeroDivisionError:
#         print('Error: invalid argument.')
# print(spam1(2))
# print(spam1(12))
# print(spam1(0))
# print(spam1(1))
#
# RETURN A DICTIONARY
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jane', 'lee', 30)
print(musician)


# using function with while loop
# def get_formatted_name(first_name, last_name):
#     """Return full name, neatly formatted"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# PASS A LIST
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# write two functions
# one handle design printing, the other summarizes prints made
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
 Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing models:" + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


# PASS AN ARBITRARY NUMBER OF ARGUMENTS, AND POSITIONAL ARGUMENTS
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""Build a dictionary containing everything we know about a user."""
def print_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile
# user_profile = print_profile('albert', 'einstein',
#                              location ='princeton',
#                              field='physics')
# print(user_profile)
print(print_profile('albert', 'einstein',
                              location ='princeton',
                              field='physics'))
