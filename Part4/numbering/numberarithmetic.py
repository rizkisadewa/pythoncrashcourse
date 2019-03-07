# Arithmetic

from fractions import Fraction
a = Fraction(1, 4) # 1/4
b = Fraction(2, 4) # 2/4

print(a)

# additions the fraction
c = a + b
print(c)
print(type(c))

# reductions the fraction
d = 1 - b
print(d)

# multiplication the fraction
e = a * b
print(e)

x = Fraction(3, 8)
print(x)
print(x.numerator) # numerator of Fraction
print(x.denominator) # denominator of Fraction

# division
print(Fraction(3, 8) / 3)
print(Fraction(1, 2) / Fraction(1, 4))

# Convert from Fraction to Decimal
print(type(x))
y = float(x)
print(y)
print(type(y))
