# Private Method

class rectangle:
    def __init__(self, l=0, w=0):
        self.__length = l
        self.__width = w

    def setvalue(self, l, w):
        self.__length = l
        self.__width = w

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def wide(self):
        return self.__length * self.__width

# Make an object
obj = rectangle()

# set value
obj.setvalue(10,8)

# get the value
print(obj.getLength())
print(obj.getWidth())

# get the value of wide
print(obj.wide())
