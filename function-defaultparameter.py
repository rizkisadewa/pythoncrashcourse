# Default Parameter in a Function
def sortinglist(lst, reversing=False):
    lst.sort(reverse=reversing)

a = [20, 10, 40, 50, 60, 5]

sortinglist(a)
print(a) # without Parameter reversing

sortinglist(a, True)
print(a) # with Parameter reversing
