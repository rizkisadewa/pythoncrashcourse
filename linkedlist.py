# Linked list

# node class
class node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

# linked list class container
class linkedlist:
    def __init__(self):
        # refer to the first node
        self.head = None
        # refer to the last node
        self.tail = None
        self.size = 0 # zero in the beginning

    # checking size of list
    def isempty(self):
        return self.size == 0

    # adding node to the first position
    def addfirst(self, element):
        # new node (newnode.next refer to the head)
        newnode = node(element, self.head)
        # head refer to the new node
        self.head = newnode
        # Add the size of node
        self.size += 1
        # if the list is only contain one
        if self.tail == None:
            self.tail = self.head

    # Obtain the element from the first node
    def getfirst(self):
        if self.isempty():
            return None
        else:
            return self.head.element

    # deleting first node
    def removefirst(self):
        if not self.isempty():
            temp = self.head
            self.head = self.head.next
            self.size -+ 1 # reduct the size of list
            del temp # optional

    # adding the node in the last position
    def addlast(self, element):
        # make a new node (newnode.next assigned zero)
        newnode = node(element)
        if self.tail == None: # if the list still empty
            self.head = newnode # head refer to the newnode
            self.tail = self.head # tail refer to the head
        else: # if list filled
            # relate the last node to the newnode
            self.tail.next = newnode
            # move the tail for the reference to the newnode
            self.tail = self.tail.next
        self.size +=1

    # obtain the element to the last node
    def getlast(self):
        if self.isempty():
            return None
        else:
            return self.tail.element

    # removing the last node
    def removelast(self):
        if not self.isempty():
            if self.size == 1:
                temp = self.head
                self.head = None
                self.tail = None
                self.size = 0
                del temp
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                temp = self.tail
                self.tail = current
                self.tail.next = None
                self.size -= 1
                del temp

    # showing the elements which the node inside the list
    def __str__(self):
        s ='['
        current = self.head
        while current != None:
            s += str(current.element)
            if current != self.tail:
                s += ', '
            current = current.next
        s += ']'
        return s
    def __repr__(self):
        return self.__str__()

# *** Make and object ***
llist = linkedlist()

# adding the element with addfirst()
llist.addfirst('Python')

# adding the element with addlast()
llist.addlast('Ruby')
print(llist)

# adding the element with addfirst()
llist.addfirst('C++')

# adding the element with addlast()
llist.addlast('PHP')
llist.addlast('Java')
llist.addlast('Perl')

print(llist)

# obtaining the first element
print(llist.getfirst())

# obtaining the last element
print(llist.getlast())

# deleting the first element
llist.removefirst()
print(llist)

# deleting the last element
llist.removelast()
print(llist)