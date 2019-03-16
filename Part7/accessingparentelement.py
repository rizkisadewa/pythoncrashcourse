# Accessing Parent Attribute and Methods

# Parent Class
class parent:
    def __init__(self, x):
        self.x = x

    def printx(self):
        print('X value : %d'% self.x)

# Child Class
class child(parent):
    def __init__(self, x, y):
        # call parent.__init__()
        super().__init__(x)
        self.y = y

    def printy(self):
        print('Y value : %d'% self.y)

    def printxy(self):
        # call parent.printx()
        super().printx()

        # call child.printy() method
        self.printy()

# Make an object
obj = child(100, 200)

# call method printxy
obj.printxy()
