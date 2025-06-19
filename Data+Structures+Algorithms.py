# Sequence types are string, list and tuple
# Indexing
# 1 string
string1 = "Programming"
print(string1[0])

# 2 list
list1 = ['pig', 'cow', 'frog']
print(list1[1])

# 3 tuple
tuple1 = ('Kevin', 2, 'Jenny', 'Craig')
print(tuple1[2])

# Slicing
# [start:end+1:step]
string2 = "Computer"
print(string2[1:4])
print(string2[1:6:2])
print(string2[3:])
print(string2[:5])
print(string2[-1])
print(string2[-3])
print(string2[:-2])

# Adding and Concatenating
# string
x = 'horse' + 'shoe'
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

# tuple
z = ('Kevin', 'Niklas', 'Jenny') + ('Craig',)
print(z)

# Multiply a sequence using *
# string
a = 'Apple' * 3
print(a)

# list
b = [8, 5]*3
print(b)

# tuple
c = (2, 4) * 3
print(c)

# Checking membership
# string
d = 'bug'
print('u' in d)

# list
e = ['pig', 'cow', 'horse']
print('cow' not in e)

# tuple
f = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print('Niklas' in f)

# Iterating throgh the items in a sequence
# item
g = [7, 8, 3]
for item in g:
    print(item)

# index and item
h = [7, 8, 3]
for index, item in enumerate(h):
    print(index, item)
    
# Number of items - count the number of items in a sequence
# string
i = 'bug'
print(len(i))

# list
j = ['pig', 'cow', 'horse']
print(len(j))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(len(k))

# Minimum - find the minimum item in a sequence lexicographically
# Alpha or numeric types , but cannot mix types
# string
l = 'bug'
print(min(l))

# list
j = ['pig', 'cow', 'horse']
print(min(j))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(min(k))

m = [65, 'A', 0]
#print(min(m))

# Maximum - find the maximum item in a sequence lexicographically
# Alpha or numeric types , but cannot mix types
# string
l = 'bug'
print(max(l))

# list
j = ['pig', 'cow', 'horse']
print(max(j))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(max(k))

# Sum - find the sum of items in a sequence
# Entire sequence must be numeric
# string => error
# list
y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))

# tuple
z = (50, 4, 7, 19)
print(sum(z))

# Sorting - returns a new list of items in sorted order
# Does not change the original sequence
# string
x = 'bug'
print(sorted(x))

# list
j = ['pig', 'cow', 'horse']
print(sorted(j))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(sorted(k))

# Count(items) - returns count of an item
# string
x = 'hippo'
print(x.count('p'))

# list
j = ['pig', 'cow', 'horse', 'cow']
print(j.count('cow'))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(k.count('Kevin'))

# Index(item) - returns the index of the first occurence of an item
# string
x = 'hippo'
print(x.index('p'))

# list
j = ['pig', 'cow', 'horse', 'cow']
print(j.index('cow'))

# tuple
k = ('Kevin', 'Niklas', 'Jenny', 'Craig')
print(k.index('Jenny'))

# Unpacking - unpack the n items of a sequence into n variables
j = ['pig', 'cow', 'horse', 'cow']
a, b, c, d = j
print(a, b, c, d)