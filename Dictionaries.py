# Dictionaries (dict)
'''
Key/value pairs
Associative array, like Java HashMap
Dicts are unordered
'''

# Create dictionaries
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(x)

y = dict([('pork',25.3), ('beef',33.8), ('chicken',22.7)])
print(y)

z = dict(pork=25.3, beef=33.8, chicken=22.7)
print(z)
z['shrimp'] = 38.2 # add or update
print(z)

# delete an item
del(z['shrimp'])
print(z)

# get length of dict
print(len(z))

# delete all items from dict
z.clear()
print(z)

# delete dict
del(z)

# Access keys and values in a dict
y = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(y.keys())
print(y.values())
print(y.items())

# check membership in y_keys
print('beef' in y)

# check membership in y_values
print('clams' in y.values())

# Iterating a dict - notes, items are in random order
for key in y:
    print(key, y[key]) # return key-value pairs

for k, v in y.items():
    print(k, v) # return key-value pairs