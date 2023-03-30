# filename = 'pi_digits.txt'
# #read a file
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# #is your birthday contained in pi
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# # birthday = input("ENter your birthday, in mmddyy:")
# # if birthday in pi_string:
# #     print("Your birthday appears in the first million digits of pi")
# # else:
# #     print("Your birthday does not appear in the first million digits of pi")
# print(pi_string)
# print(len(pi_string))
#
# #write to a file
# with open(filename, 'w') as file_object:
#     file_object.write("I love programming\n")
#     file_object.write("I love creating new games.\n")
#
# #append to a file
# with open(filename, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")
#     file_object.write("I love creating apps that can run in a browser.\n")


#EXCEPTIONS
#ZeroDIvisionError

# try:
#  print(5/0)
# except ZeroDivisionError:
#  print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# # while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#        answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

#FileNotFoundError
# filename = 'alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)

# title = "Alice in Wonderland"
# print(title.split())

#ANALYZING TEXT FILES
filenames = ['alice.txt', 'pi_digits.txt', 'siddarth.txt']
def count_words(filename):
    """ Count the approximate number of words in the file."""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
    #fall silently
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
for filename in filenames:
    count_words(filename)