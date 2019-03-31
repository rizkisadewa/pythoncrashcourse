# Insertion Sort
def insertionsort(alist):
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue

# Implementation
data = [12, 10, 6, 11, 5, 4, 7, 9, 8]

# Calling function insertionsort()
insertionsort(data)
print(data)