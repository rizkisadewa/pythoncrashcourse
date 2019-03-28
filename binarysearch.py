# Binary Search
def binarysearch(alist, value):
    if len(alist) == 0:
        return False
    else:
        middle = len(alist) // 2
        if alist[middle] == value:
            return True
        else:
            if value < alist[middle]:
                return binarysearch(alist[:middle], value)
            else:
                return binarysearch(alist[middle:1], value)

# Sample
data = [100, 200, 300, 400, 500, 600]

# Searching 200
print(binarysearch(data, 200))
print(binarysearch(data, 550))

'''
to use Binary Search, we need to sort the list. 

'''

