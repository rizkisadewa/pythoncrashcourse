# Linear Search or Sequential Search
def sequentialsearch(alist, value):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == value:
            found = True
        else:
            pos += 1
    return found

# modified 2
def sequentialsearch2(alist, value):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == value:
            found = True
        else:
            pos += 1
    if found:
        return pos # if found
    else:
        return -1 # if not found

# modified 3
def sequentialsearch3(alist, value):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not stop and not found:
        if alist[pos] == value:
            found = True
        else:
            if alist[pos] > value:
                stop = True
            else:
                pos += 1
    return found

# implementation
data = [300, 200, 500, 400, 100]
data1 = [100, 200, 300, 400, 500]

# searching 400 value
print(sequentialsearch(data, 400))
print(sequentialsearch2(data, 250)) # -1 means that the value not found in the data
print(sequentialsearch3(data1, 250))


'''
the method modified number 1 and 2 is for the data which is not in sort.
therefore if the data has been sorted, you can use the method modified number 3
'''

