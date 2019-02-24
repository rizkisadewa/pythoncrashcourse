# Set
a = [10, 20, 30] # a list
s = set(a)
print(s)

b = [10, 20, 10, 10, 30, 40, 20]
s1 = set(b)
print(s1)

'''
make a unique dictionary
'''

# Accessing a Set
# Option 1, extract to variable
c, d, e = s
print(c, d, e)

# Option 2, convert to list
print(list(s)[2])

# Adding value into Set
# Option 1, use an add()
s.add(300)
print(s)

# Option 2, use an update() method
s.update([40,60,70])
print(s)

# Deleting set value
# option 1, use a discard() method
s.discard(20)
print(s)

# option 2, use a clear() method to delete all the value
s.clear()
print(s)

# Editing Element Set
s = set([10,20,30])
print(s)
s.discard(30)
s.add(50)
print(s)
