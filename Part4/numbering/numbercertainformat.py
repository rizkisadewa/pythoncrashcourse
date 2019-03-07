# show the certain format
x = 123.456789

# show x with two digit decimal
print(format(x, '0.2f'))

# show rounding number
print(format(x, '0.0f'))

# left align x with 1 decimal and the space with 10 character size
print(format(x, '<10.1f'))

# justify x with 1 decimal and the space with 10 character size
print(format(x, '^10.1f'))

# right align with 1 decimal and the space with 10 character size
print(format(x,'>10.1f'))
#or we can use below
print(format(x,'10.1f'))

#using __format__()
print(x.__format__('0.2f'))
print(x.__format__('0.0f'))
print(x.__format__('<10.1f'))
print(x.__format__('^10.1f'))
print(x.__format__('>10.1f'))
print(x.__format__('10.1f'))

# eksponantial
print(format(x, 'e'))
print(format(x, '0.2E'))
