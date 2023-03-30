string1 = 'Alice'
string2 = ' in '
string3 = ' Wonderland.'
int1 = 5
concat_string = string1 + string2 + string3
print(concat_string)

string_replicate = 'Eggs' * 4
print(string_replicate)

r_string = (r"Hello\tJane")
print(r_string)

#   multiline
multi_string  = """This is a mutiline 
string
has nothing to do with me"""
multi_string2 = '''this 
is also good'''
print(multi_string)
print(multi_string2)
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com
This program was designed for Python 3, not Python 2.
"""

slice_string = 'Hello'
print(slice_string[0])
print(slice_string[-1])
print(slice_string[2:4])

checker = 'chocolate' not in 'Some chocolate'
print(checker)

convert_string = 'baseball'
print(convert_string.upper())
check_string = 'Hi Jane'
print(check_string.isupper())
print(check_string.islower())