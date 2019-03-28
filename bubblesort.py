# Bubble Sort
def bubblesort(alist):
    for i in range(0, len(alist)-1):
        print('Langkah ke-%d: '% (i+1), end='')
        for j in range(len(alist)-1, i, -1):
            if alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
        print(alist)

data = [9, 7, 10, 8, 12, 11, 14, 13]

# showing the data
print(data)

# calling bubblesort()
bubblesort(data)
print(data)

'''
we can code simpler, 
alist[j], alist[j-1] = alist[j-1], alist[j]
'''