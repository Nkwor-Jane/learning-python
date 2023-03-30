# messgae = input("Tell me your age?")
# print(messgae)

# prompt = "Show me your friends and i wil tell you who you are."
# prompt += "\n What's yur best friend's name? "
#
# name = input(prompt)
# print("\n Hello, " + name)
#
# age = input("How old are you?")
# age = int(age)
# age >= 18

current_num = 2
while current_num < 20:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#USING A WHILE LOOP WITH LISTS AND DICTIONARIES
#MOVE ITEMS FROM ONE LIST TO ANOTHER
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = [ 'alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)