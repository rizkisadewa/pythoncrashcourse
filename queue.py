# Queue of the list
class queue:
    def __init__(self):
        self.__data = []
        self.__size = 0
        self.__front = 0 # position in the front

    # Method for showing total queue element
    def __len__(self):
        return self.__size

    # Method for checking queue, whether empty or not
    def isempty(self):
        return self.__size == 0

    # Method for obtaining the first element
    def first(self):
        if self.isempty():
            raise Exception('The queue is empty ...')
        return self.__data[self.__front]

    # Method for adding the element into the queue
    def enqueue(self, element):
        self.__data.append(element)
        self.__size += 1

    # Method for calling the first element
    def dequeue(self):
        if self.isempty():
            raise Exception('The queue is empty...')
        result = self.__data[self.__front]
        del self.__data[self.__front]
        self.__size -= 1
        return result

    # Method for showing the queue element
    def __repr__(self):
        return repr(self.__data)


# make an object from queue class
q = queue()

# adding the element into the queueu
q.enqueue('Python')
q.enqueue('Java')
q.enqueue('CSS')
q.enqueue('HTML')
q.enqueue('Javascript')

# showing the queue lement
print(q)

# showing the element total
print(len(q))

# obtain the first element
print(q.first())