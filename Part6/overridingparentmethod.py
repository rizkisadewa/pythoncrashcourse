# Override parent method

# parent class
class parent:
    def method1(self):
        print("This is Parent Method 1")

    def method2(self):
        print("This is Parent Method 2")

# Child Class
class child(parent):
    # do overriding parent method
    def method2(self):
        print("This is Child Method 2")

# Make an object
obj = child()

# call parent parent.method1
obj.method1()

# call child child.method2
obj.method2()

'''
Or if we want to keep the parent element , you can do below
'''
# parent2 class
class parent2:
    def method1(self):
        print("This is Parent2 Method 1")

    def method2(self):
        print("This is Parent2 Method 2")

# pchild2 class
class child2(parent2):
    # Example overriding methodexample
    def method1(self):
        # keep the parent2 behavior
        super().method1()
        # additional code block in child method
        print("Implement additional code in child2 method")

# make an object
obj2 = child2()

# accessing method1
obj2.method1()
