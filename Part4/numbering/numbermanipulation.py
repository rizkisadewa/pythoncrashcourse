# Rouding Number

x = 12.345678

print(round(x,1)) # rounding only one decimal
print(round(x,2)) # rounding with two decimal
print(round(x)) # ndigits will given zero, no ndigits

'''
Prototype :
round(number[, ndigits]) -> number
number is the amount that would be rounded
ndigits is to declare how many digits that would be given in the number. The default is zero.
'''


# Decimal Convert to Binary and v.v.
a = 10
s = bin(a)
print(s)
print(int(s, 2)) # converted again to decimal

'''
0b means has been converted to binary
'''

# Decmal Covert to Octal and v.v.
b = 16
s1 = oct(b)
print(s1)

j = 0o10
print(j*2) # auto convert to decimal

'''
0o means has been converted to Octal
'''

# Convert Decimal to Hex
a = 64
s = hex(a)
print(s)
print(type(s))

a = 0x40
print(a//4)
print(type(a//4))
'''
0x40 means hex type
'''

# Convert String to Number
s1 = '123'
i = int(s1) # convert to integer
print(i)
print(type(i))

s2 = '123.45'
f = float(s2)
print(f)
print(type(f))

# c = input('Masukkan bilangan bulat : ')
# print(c) # show the variable c but input() default convert to string
# d = float(c) * 2 # convert to float then multiple by 2
# print(d)

# convert Decimal to String
x = 123
print(x)
print(type(x))

s1 = str(x)
print(s1)
print(type(s1))

y = 123.45
print(y)
print(type(y))
s2 = str(y)
print(s2)
print(type(s2))
