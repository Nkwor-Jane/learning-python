# guest_lists = ['Steve Jobs', 'King David', 'Elijah', 'Joyce Meyer', 'Donald Trump']
# print('Hi {}, I would like to invite you to my dinner party'.format(guest_lists[0]))
# print('Hi {}, I would like to invite you to my dinner party'.format(guest_lists[1]))
# print('Hi {}, I would like to invite you to my dinner party'.format(guest_lists[2]))
# guest_lists.insert(0, 'Prophet Samuel')
# guest_lists.insert(3, 'Hansel')
# guest_lists.append('Park Rachel')
# print(len(guest_lists))
# print('Hi {}, I have found a bigger dinning room.I would like to invite you to my dinner party, the more the merrier'.format(guest_lists[0]))
# print('Hi {}, I have found a bigger dinning room.I would like to invite you to my dinner party, the more the merrier'.format(guest_lists[2]))
# # print(sorted(guest_lists))
# print(guest_lists)
# sorted_list = guest_lists.reverse()
# print(sorted_list)
# print(guest_lists[:])
#
# for guest in guest_lists:
#     print(f"Hi, {guest} I would like to invite you to my dinner party")
#     print(f"i found a band that plays jazz, i am sure {guest} and i will have a good time")
#     print('Thank you for coming, it was a great party\n')
# numbers = list(range(2, 11, 2))
# print(numbers)
# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))
# # LIST COMPREHENSION -- GENERATE LIST WITH A LINE OF CODE
# ones = [value for value in range(1, 20, 2)]
# print(ones)
# print(min(ones))
# print(max(ones))
# print(sum(ones))
#
# my_foods = ['pizza', 'falafel', 'cake']
# my_foods.append('apples')
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite are: ")
# print(friend_foods)
#
# dimensions = (20, 30)
# for dimension in dimensions:
#     print(dimension)

# name =''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('DOne')

# this will be 100 iterations where 0-100 will have been added to make a total
#sum of all numbers from 1 -100 is 5050
total = 0
for num in range(101):
    total = total + num
print(total)
