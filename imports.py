import random,sys

for i in range(5):
    print(random.randint(1, 20))


while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')