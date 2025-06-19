# Lists
'''
They are general purpose data type
Most widely used data structure
Grow and shrink size as needed
They're sequence type
They are sortable
Constructor - creating a new list
'''

# Create lists
x = list() # List constructor
y = ['a', 25, 'dog', 8.43]
tuple1 = (10, 20)
z = list(tuple1) # List from tuple

# Through list comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i>4]
print(b)

# Delete items from list
x = [5, 3, 8, 9]
del(x[1]) # deletes the second item on the list and create a new list
#print(x)
#del(x) # list no more exists
#print(x)

# Append - append an item to a list
x = [5, 3, 8, 9]
x.append(7) # add items to the tale end
print(x)

# Extend - append a sequence to a list
x = [5, 3, 8, 9]
y = [12, 13]
x.extend(y)
print(x)

# Insert - insert an item at a given index
x = [5, 3, 8, 9]
x.insert(1, 7) # insert 7 at the 1th position
print(x)
x.insert(1, ['a', 'm']) # insert a list at a given index
print(x)

# Pop - pops last item off list and returns item
x = [5, 3, 8, 9]
x.pop()
print(x)
print(x.pop())

# Remove - remove first instance of an item
x = [5, 3, 8, 9, 3]
x.remove(3)
print(x)

# Reverse - reverse the order of the list.
# It is an in-place sort, meaning it changes the original list
x = [5, 3, 8, 9]
x.reverse()
print(x)

# Sort - sort the list in place
# sorted(x) returns a new list without changing the original list x
# x.sort() puts items of x in sorted order (sorts in place)
x = [5, 3, 8, 9]
x.sort()
print(x)
x.sort(reverse = True)
print(x)
