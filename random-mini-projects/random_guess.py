"""Create simple guessing game that allows
user to randomly pick a number from 1-100"""

from random import randint

secret_number = randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")

    # Prompt the user to continue or quit
    print("Enter q to quit, or any other key to continue: ")
    choice = input()
    if choice.lower() == "q":
        break