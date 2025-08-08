from random import randrange

random_num = randrange(20, 101)

name = input('Enter name: ')

if name == '':
    name = 'Teddy'

print(f'{name} is {random_num} years old!')