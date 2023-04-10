def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

numbers = [2, 5, 6, 1.5, -1.0]
for a in numbers:
    ans = (add_integer(a))
    print(ans)

print(add_integer(4600, -7))
print(add_integer(2**5, 2))
print(add_integer(-8.5, 5))
print(add_integer(2.0**3.0, 5))
# print(add_integer())
# print(add_integer(2,3,4))
# print(add_integer(6, "another"))
print("matrix must be a matrix(list of lists) of integers\\floats")