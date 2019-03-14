class rectangle:
    def __init__(self, l, w):
        self.__length = l
        self.__width = w
    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, l):
        self.__length = l

    @width.setter
    def width(self, w):
        self.__width = w

    def size(self):
        return self.__length * self.__width


# Make an object
obj = rectangle(10,8)

# call property lenght
print(obj.length)

# call propoerty width
print(obj.width)

'''
If we asign lik obj.length = 10 , error will be given by the mechine 
therefore we need to have setter 
'''
obj.length = 3
print(obj.length)

obj.width = 5
print(obj.width)