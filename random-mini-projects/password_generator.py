import random
import string

def generate_password(length):
    """Function to generate random password of a given length,
    using a combination of uppercase letters, lowercase letters,
    digits and special characters"""

    # define string to contain all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # generate password using random selection
    passwrd = "".join(random.choice(all_chars) for i in range(length))
    return passwrd


while True:
    # Prompt for password length
    print("Enter preferred password length: ")
    length = int(input())

    if length <= 5:
        print(f"Password must exceed 5 characters for it to be safe")

    result = generate_password(length)
    print(result)

    # Prompt the user to continue or quit
    print("Enter q to quit, or any other key to continue: ")
    choice = input()
    if choice.lower() == "q":
        break
# test function
# password = generate_password(4)
# print(password)