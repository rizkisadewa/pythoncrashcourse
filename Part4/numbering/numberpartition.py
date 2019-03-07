# Number Partition
x = 123455667788
print(format(x, ','))

# Partition with coma and dot
def thousand(a, partition=','):
    lst = list(str(a))
    n = len(lst) - 3
    while n > 0:
        lst.insert(n, partition)
        n -= 3
    return ''.join(lst)

print(thousand(x))
print(thousand(x, '.'))
