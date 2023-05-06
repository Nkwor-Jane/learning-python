"""Password checker to check if a 
password is strong enough based on some
criteria we will set"""


# Define function to check if password is strong enough
def password_checker(password):
    # define criteria
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"

    # password length
    if len(password) < min_length:
        print("Password is too short!")
        return False
    # Check is password fulfills criteria
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False

    # print success message if criteria are met
    print("Password is strong!")
    return True


# Prompt user to enter a password and check if it meets the criteria
password = input("Enter a password: ")
password_checker(password)
