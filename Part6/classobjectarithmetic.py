# Class Object Arithmetic
class number:
    def __init__(self, value):
        if isinstance(value, int) or \
            isinstance(value, float):
                self.value = value
        else:
            raise TypeError('Parameter name must in number type')

    # overload operator +
    def __add__(self, x):
        if isinstance(x, number):
            return self.value + x.value
        elif isinstance(x, int):
            return int(self.value) + x
        elif isinstance(x, float):
            return float(self.value) + x
        else:
            raise TypeError('Parameter name must in number type')

    # overload operator -
    def __sub__(self, x):
        if isinstance(x, number):
            return self.value - x.value
        elif isinstance(x, int):
            return int(self.value) - x
        elif isinstance(x, float):
            return float(self.value) - x
        else:
            raise TypeError('Parameter name must in number type')

    # overload operator *
    def __mul__(self, x):
        if isinstance(x, number):
            return self.value * x.value
        elif isinstance(x, int):
            return int(self.value) * x
        elif isinstance(x, float):
            return float(self.value) * x
        else:
            raise TypeError('Parameter name must in number type')

    # overload operator /
    def __truediv__(self, x):
        if isinstance(x, number):
            return self.value / x.value
        elif isinstance(x , int):
            return int(self.value) / x
        elif isinstance(x, float):
            return float(self.value) / x
        else:
            raise TypeError('Parameter name must in number type')

# Make the object of number
a = number(10)
b = number(3)

# operation between two object
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# operation with int
print(a+2)
print(a-6)
print(a*3)
print(a/2)

# operation with float
print(a+3.5)
print(a-2.5)
print(a*2.0)
print(a/2.5)