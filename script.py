# functional

name_lengths = map(len, ['Mary', 'Ana', 'Sam', 'Isla'])
print(list(name_lengths))


# map that squares every number in a passed collection

squares = map(lambda x : x**2, [1,2,3,4,5,6,7,8,9])
print(list(squares))

def exponential(y) :
    return lambda  x : x**y

squares = map(exponential(2),[1,2,3,4,5,6,7,8,9])
print(list(squares))

cubes = map(exponential(3),[1,2,3,4,5,6,7,8,9])
print(list(cubes))

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

# takes a list of names and replace them with randomly assigned code_names

anonymized_names = list(map(lambda name : random.choice(code_names),names))
print(anonymized_names) 

# takes a list of names and replace them with their hash values

hashed_names = list(map(hash,names))
print(hashed_names)

from functools import reduce

# returns the sum of all items in a collection

sum = reduce(lambda accumulator,value : accumulator + value,[1,2,3,4])
print(sum)

# counts the occurrence of 'Sam' in the following list
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

number_of_sams = reduce(lambda accumulator, item : accumulator + item.count('Sam'), sentences,0)
print(number_of_sams) 


# calculates the average of height in a list of key-value pairs

people = [  {'name': 'Mary', 'height': 160},
            {'name': 'Isla', 'height': 80},
            {'name': 'Sam'}]

heights = list(map(lambda dict : dict['height'],filter(lambda dict : 'height' in dict ,people)))

average_height = reduce(lambda acc, value : acc + value, heights) / len(heights)

print(average_height)


# Describe HOW to do = Imperative
from random import random
time = 5
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1

    print('')
    for i in range(len(car_positions)):
        # move car
        if random() > 0.3:
            car_positions[i] += 1

        # draw car
        print ('-' * car_positions[i])



