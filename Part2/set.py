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

# Copying Set
s2 = set([10,20,30])
print(s2)
s3 = s2.copy()
print(s3)

# Slicing Set
# Using intersection()
s4 = set([1,2,3,4,5])
print('set s4 : ', s4)
s5 = set([3,5,7])
print('set s5 : ', s5)
s6 = s4.intersection(s5)
print('intersection s4 & s5: ', s6)

# The different between set
s7 = s4.difference(s5)
print('the difference s4 & s5: ', s7)

# Combine betweeen two lists
s8 = s4.union(s5)
print('combining s4 and s5 : ', s8)

# Constant set, cannot be added or modified
fs = frozenset([10,20,30])
for i in fs:
    print(i)
'''
frozen will make a set cannot be deleted, added or modified
'''
