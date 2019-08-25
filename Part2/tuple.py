# Tuple
# every single element canot be changed

t = (100, 200, 300, 400, 500)

# Accessing the tuple

print(t[1])
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

'''
if we asign the value in tuple, the system will error
'''

# Searching Index
ind = t.index(100)
print('index 100 is ', ind)

minimum = min(t)
print('Nilai minimum adalah %d, beradada pada indeks ke-%d' % (minimum, t.index(minimum)))

maximum = max(t)
print('Maximum value is %d, in index at %d' % (maximum, t.index(maximum)))

'''
We can also use the index for the above method
'''

# Counting Element in Tuple
t2 = (10,20,10,30,10,40,20)

print(t2.count(10))
print(t2.count(20))
