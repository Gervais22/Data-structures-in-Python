'''
Tuples are immutable
They are used for fixed data
They are faster than Lists
They are sequence type
'''

# Create a new tuple
x = ()
x = (1, 2, 3)
x = 1, 2, 3 # Python still knows it's a tuple
x = 2, # a single item tuple should have a comma after the item
list1 = [1, 4, 6]
x = tuple(list1) # Create a tuple out of a list
print(x, type(x))

# Tuples are immutable
# But member objects can be mutable
x = (1, 2, 3)
#del(x([1])) # fails
#x([1]) = 8 # fails

y = ([1, 2], 3) # a tuple where the first item is a list
# del(y([0][1])) # delete the 2
print(y)

y += (4,) # concatenating a tuple and another tuple
print(y)