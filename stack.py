# Stack
class stack:
    def __init__(self):
        # make an empty stack
        self.__data = []

    # method for showing total element stack component
    def __len__(self):
        return len(self.__data)

    # Method for checking whether empty or there is component inside
    def isempty(self):
        return len(self.__data) == 0

    # method for adding element
    def push(self, element):
        self.__data.append(element)

    # Method for showing the top element
    def top(self):
        if self.isempty():
            raise Exception('Stack empty')
        return self.__data[-1]

    # Method to take out the element on the top
    def pop(self):
        if self.isempty():
            raise Exception('Empty stack')
        return self.__data.pop()

    # Method for representing an object stack in string
    def __repr__(self):
        return repr(self.__data)

# make an object from stack class
s = stack()

# add the element to the stack
s.push('Python')
print(s)

# Add again the new two element to the stack
s.push('Ruby')
s.push('Java')
print(s)

# get the last element from the top
print(s.top())

# take out the last element from the top
s.pop()
print(s)

# get the information of the total element
print(len(s))

'''
Stack has the method like LIFO (Last In First Out)
'''