# Filtering List
a = [1,-3,4,-2,5,7,-4]
b = [1,2,3,4,5,6]

# Filtering Negative Number
negatif = [i for i in a if i < 0]
print(negatif)

# Filtering positive number
positive = [i for i in a if i > 0]
print(positive)

# Filtering ganjil genap
c = ['genap' if i % 2 == 0 else 'ganjil' for i in b]
print(c)

# Filtering square number
square = [i**2 for i in b]
print(square)
