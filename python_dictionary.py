# Dictionaries
dict1 = {
    'name': 'Amol', 'city': 'pune', 'age': 25
}
print(dict1)

# Access Items
dict2 = {
    'name': 'Amol', 'city': 'pune', 'age': 25
}
print(dict2['name'])
print(dict2['city'])

# using Get() method
dict3 = {
    'name': 'Amol', 'city': 'pune', 'age': 25
}
print(dict3.get('name'))
print(dict3.get('age'))

# change value
dict4 = {'name': 'Amol', 'city': 'pune', 'age': 25}
dict4['city'] = 'mumbai'
print(dict4)

# Loop with dictionary
dict5 = {'name': 'Amol', 'city': 'pune', 'age': 25}
for values in dict5:
    print(values)

# Loop with dictionary
dict6 = {'name': 'Amol', 'city': 'pune', 'age': 25}
for values in dict6:
    print(values)

# FETCH BOTH KEYS AND VALUES
dict7 = {'name': 'Amol', 'city': 'pune', 'age': 25}
for a, b in dict7.items():
    print(a,b)

# delete dict
dict8 = {'name': 'Amol', 'city': 'pune', 'age': 35}
del dict8
print(dict8)