a = [10,20,30]

# add with append() method
a.append(40)
print(a)

# add with insert() method
a.insert(2, 50)
print(a)

# with method extend()
a.extend([66,77,88])
print(a)

# append will always count a data as one data
b = [10,20]
b.append([30,40])
print(b)

# if list added by extend() method, the string will be input per caracter
c = [10,20,30]
c.extend("Hellow World")
print(c)
