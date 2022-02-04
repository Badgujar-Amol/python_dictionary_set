# Accessing set member
s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90,100}
print(s1)

s2 = {10, 20, 30, 40, 50, 60, 70, 80, 90}
for number in s2:
    print(number)

# check values
s3 = {'om', 'arjun', 'karan', 'satish', 'jay' }
print('ramesh' in s3)

s4 = {'om', 'arjun', 'karan', 'satish', 'jay' }
print('ramesh' not in s4)

# Add item in set
s5 = {'om', 'arjun', 'karan', 'satish', 'jay' }
s5.add('ramesh')
print(s5)

# check length of set
s6 = {'om', 'arjun', 'karan', 'satish', 'jay' }
print(len(s6))

# delete set
s7 = {'om', 'arjun', 'karan', 'satish', 'jay' }
del s7


# union() method of set
s8 = {1,2,3,4,5}
s9 = {6,7,8,9,10}
values = s8.union(s9)
print(values)

# intersection of set
i = {1,2,3,4,5,7,9}
j = {5,4,6,7,8,9,10}
add = i & j
print(add)

# Difference of set
a = {1,2,3,4,5,7,9}
b = {5,4,6,7,8,9,10}
diff = a - b
print(diff)


a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}
c = a | b
print(c)