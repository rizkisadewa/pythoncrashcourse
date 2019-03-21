# Inheritance Class
class intlist(list):

    '''
    (list) is the parent class
    we ovveride the method append(), insert() and exend(), we added excetion TypeError in those methods
    and we also added the checking method in insert() and extend() which is only int allowed
    '''

    # Restrict element list total
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0

    # Check list element total whether empty or not
    def isempty(self):
        return self.size == 0

    # Check list element total whether full or not
    def isfull(self):
        return self.size == self.capacity

    # Checking object type when added to list
    def checktype(self, obj):
        if not isinstance(obj, int):
            raise TypeError('Element harus bilangan bulat')

    # Override list.append() method
    def append(self, obj):
        if self.isfull(): raise TypeError('List is full')
        self.checktype(obj)
        super().append(obj)
        self.size += 1

    # Override list.insert() method
    def insert(self, index, obj):
        if self.isfull(): raise TypeError('List is full')
        self.checktype(obj)
        super().insert(index, obj)
        self.size += 1

    # Override list.extend() methods
    def extend(self, lst):
        for obj in lst:
            self.append(obj)

    # Override list.remove() methods
    def remove(self, obj):
        if not self.isempty():
            super().remove(obj)
            self.size -= 1

    # Override list.pop() methods
    def pop(self, index=None):
        if index == None:
            index = self.size - 1
        if not self.isempty():
            temp = super().pop(index)
            self.size -= 1
            return temp

    # Ovveride list.clear() methods
    def clear(self):
        if not self.isempty():
            super().clear()
            self.size = 0

# Object from intlist
a = intlist(10)

# call append methods
a.append(1)
a.append(2)
a.append(3)
print(a)

# # Try to append with string
# a.append('Python') # => will give an error due to we declare the list is only for int at the above class

# call insert methods
a.insert(1,4)
print(a)

# # Try to insert string
# a.insert(1, 'Python')  => will give an error due to we declare the list is only for int at the above class

# Call Extend methods
a.extend([5,6,7])
print(a)

# # Try to extend string
# a.extend([5,'Python',7]) # => will give an error due to we declare the list is only for int at the above class


# call remove methods
a.remove(4)
print(a)

# Call Pop methods
a.pop(3)
print(a)
a.pop()
print(a)

# call clear method
a.clear()
print(a)

help(intlist)
