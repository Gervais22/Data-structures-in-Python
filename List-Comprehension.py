# Basic format: new_list = [transform sequence [filter]]
# Create a list out of another list

import random
# get values within a range
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))
print(under_10)
print(f'under_10: {under_10}')

# get square values
squares = [x**2 for x in under_10]
print(f'squares: {squares}')

# get odd numbers
odds = [x for x in range(10) if x%2 == 1]
print(f'odds: {odds}')

# get multiples of 10
tens = [x for x in range(65) if x%10 == 0]
print(f'multiples of 10: {tens}')

# get all numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek.'
nums = [x for x in s if x.isnumeric()]
print(f'nums: {nums}')

# get index of a list item
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print(f'index = {idx[0]}')

# delete an item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)