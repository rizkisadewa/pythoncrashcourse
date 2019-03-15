# Method Static
class arithmetic:
    @staticmethod
    def add(a, b): # not add(self, a, b):
        return a + b

    @staticmethod
    def reduce(a, b):
        return a - b

    @staticmethod
    def multiple(a, b):
        return a * b

    @staticmethod
    def dev(a, b):
        return a / b

# call method without make an object
# from aritmethic
print(arithmetic.add(10, 5))
print(arithmetic.reduce(10,5))
print(arithmetic.multiple(10,5))
print(arithmetic.dev(10,5))

# make an object
obj = arithmetic()

# call to method static from object
print(obj.add(3,4))
print(obj.reduce(10,5))
print(obj.multiple(10,5))
print(obj.dev(11,3))