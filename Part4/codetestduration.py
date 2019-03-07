# Test Duration for certain code

# Sorting Function
def sortlist(lst):
    for i in range(0, len(lst)-2):
        for j in range(len(lst)-1, i, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

# x = list(range(50, 0, -1))
# print(x[0-1])


# Function to count the duration
def countduration(lst):
    import time
    startingtime = time.time()
    # do a proses sorting
    sortlist(lst)
    duration = time.time() - startingtime
    return duration

# sorting example
import random
data1 = [random.randrange(0,500) for i in range(0,1000)]
data2 = [random.randrange(0,500) for i in range(0,1500)]
data3 = [random.randrange(0,500) for i in range(0,2000)]

# counting execution time
print('Sorting duration for 1000 data : %f second' % countduration(data1))
print('Sorting duration for 1500 data : %f second' % countduration(data2))
print('Sorting duration for 2000 data : %f second' % countduration(data3))
