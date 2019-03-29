# Selection Sort from lower to higher
def selectionsort(alist):
    for i in range(0, len(alist)-1):
        minposition = len(alist) - 1
        for j in range(len(alist)-2, i-1, -1):
            if alist[j] < alist[minposition]:
                minposition = j
            temp = alist[i]
            alist[i] = alist[minposition]
            alist[minposition] = temp

# implementation
data = [9, 7, 10, 8, 12, 11, 14, 12]

# calling a function that we have declared
selectionsort(data)
print(data)

# Selection Sort from higher to lower
def selectionsort2(alist):
    for i in range(len(alist)-1, 0, -1):
        maxposition = 0
        for j in range(1, i+1):
            if alist[j] > alist[maxposition]:
                maxposition = j

        temp = alist[i]
        alist[i] = alist[maxposition]
        alist[maxposition] = temp

data2 = [9, 7, 10, 8, 12, 11, 14, 12]

#calling a function that has a method from higher to lower
selectionsort2(data2)
print(data2)