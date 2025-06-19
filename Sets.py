'''
They store non-duplicate items
Very fast access vs Lists
Math Set options (union, intersect)
Sets are unordered
'''

# Set constructors - creating new sets
x = {}
y = set()
list1 = [1, 2, 3]
z = set(list1)
print(z)

# Set operations
x = {3, 8, 5}
print(x)
x.add(7)
print(x)
x.remove(3)
print(x)

# Get length of set x
print(len(x))

# Check membership in x
print(5 in x)

# pop random item from set x
print(x.pop(), x)

# Delete all items from a set
x.clear()
print(x)

# Mathematical operations
'''
intersection (AND): set1 & set2
union (OR): set1 | set2
symmetric difference (XOR): set1 ^ set2 difference (in set1 not in set2): set1 - set2
subset (set2 contains set1): set1 <= set2
superset (set1 contains set2): set1 >= set2
'''

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s2 - s1)
print(s1 <= s2)
print(s1 >= s2)
