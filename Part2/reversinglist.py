a = [50,10,40,20,30]
a.reverse()
print(a)

#using own method
def ownReverse(lst):
    temp = []
    for element in lst[::-1]:
        temp.append(element)
    return temp

# usage
x = [50,10,20,40,30]
c = ownReverse(x)
print(c)

# lst[::1] digunakan untuk proses penelusuran mundur
