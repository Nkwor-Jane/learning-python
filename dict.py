# # alien_0 = {'color': 'green', 'points': 5}
# # print(alien_0['color'])
# # new_points = alien_0['points']
# # print("You just earned " + str(new_points) +" points!")
# # alien_0['x'] = 0
# # alien_0['y'] = 25
# # alien_0[6] = 'six'
# # del alien_0['points']
# # print(alien_0)
# #
# # #track an alien's current position that can move at different speeds
# # alien_0 = {'x': 0, 'y': 25, 'speed':'medium'}
# # print('Original x-position: ' + str(alien_0['x']))
# #
# # #move alien to the right
# # #determine how far to move alien based on current speed
# # if alien_0['speed'] == "slow":
# #     x_increment = 1
# # elif alien_0['speed'] == 'medium':
# #     x_increment = 2
# # else:
# #     x_increment = 3
# #     #new position is the old plus increment
# # alien_0['x'] = alien_0['x'] + x_increment
# # print("New x-position: " + str(alien_0['x']))
#
# #loop through dictionaries
# # user_0 = {
# #  'username': 'efermi',
# #  'first': 'enrico',
# #  'last': 'fermi',
# #  }
# # for key, value in user_0.items():
# #     print("\nKey: " + key)
# #     print("Value: " + value)
# # favorite_languages = {
# #  'jen': 'python',
# #  'sarah': 'c',
# #  'edward': 'ruby',
# #  'phil': 'python',
# # 'james': 'c',
# # 'gabby': 'python'
# #  }
# # friends =['phil', 'sarah']
# #
# # for name in favorite_languages:
# #     print(name.title())
# #     if name in friends:
# #         print(" Hi " + name.title() + ", I see your favorites languages is "
# #               + favorite_languages[name].title() + "!")
# #     if 'erin' not in favorite_languages:
# #         print("Erin, please take our poll!")
# #
# # # loop through dictionary in order
# # for name in sorted(favorite_languages.keys()):
# #     print(name.title() + ", thank you for taking our poll.")
# #
# # #return just values
# # print("The following languages have been mentioned:")
# # for lang in set(favorite_languages.values()):
# #     print(lang.title())
#
# #NESTING
# # alien_0 = {'color': 'green', 'points': 5}
# # alien_1 = {'color': 'yellow', 'points': 10}
# # alien_2 = {'color': 'red', 'points': 15}
#
# # aliens = [alien_0, alien_1, alien_2]
# # for alien in aliens:
# #     print(alien)
#
# #automatically generate a list of aliens
# # aliens =[]
# # for alien_number in range(0, 30):
# #     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# #     aliens.append(new_alien)
# #change colr, points and speed of first three aliens
# # for alien in aliens[0:3]:
# #     if alien['color'] == 'green':
# #         alien['color'] = 'yellow'
# #         alien['speed'] = 'medium'
# #         alien['points'] = 10
# #show first 5 aliens
# # for alien in aliens[:5]:
# #     print(alien)
# # print('...')
# #show how many aliens were created
# # print("Total number of aliens: " + str(len(aliens)))
#
# #STORE LIST IN A DICTIONARY
# # pizza = {
# #     'crust': 'thick',
# #     'toppings': ['mushrooms', 'extra cheese'],
# #     }
# # print('You ordered a ' + pizza['crust'] + "-crust pizza " +
# #       "with the following toppings.")
# # for topping in pizza['toppings']:
# #     print("\t" + topping)
#
# favorite_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell'],
#  }
#
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print("\n" + name.title() + "'s favorite language is:")
#     else:
#         print("\n" + name.title() + "'s favorite languages are:")
#     for language in languages:
#         print("\t" + language.title())
#
# #dictionary in a dictionary
# users = {
#  'aeinstein': {
#  'first': 'albert',
#  'last': 'einstein',
#  'location': 'princeton',
#  },
# 'mcurie': {
#  'first': 'marie',
#  'last': 'curie',
#  'location': 'paris',
#  },
#  }
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())
#
# from func import make_pizza as mp
# mp(26, 'pineapaple', 'banana', 'cream cheese')

import func as f
print(f.print_profile('jane', 'chinchin', location='engineering', field='ml/ai'))