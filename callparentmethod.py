# Calling Parent Atribute and Method in Child class

# parent class
class parent:
    def __init__(self, x):
        self.x = x

    def printx(self):
        print('Nilai X : %d' % self.x)

# child class
def child(parent):
    def __init__(self, x, y):
        # call parent.__init__()
        super().__init__(x)
        self.y = y

    def printy(self):
        print('Nilai y : %d' % self.y)

    def printxy(self):
        # call parent.printx()
        super().printx()
        # call child.printy()
        self.printy()


# Object from child class
obj = child(100, 200)

# call printxy()
obj.printxy()
