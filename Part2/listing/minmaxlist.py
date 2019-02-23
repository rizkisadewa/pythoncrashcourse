a = [300,212,500,100,342,505,150]

# minumum in list
b = min(a)
print(b)

# maximum in list
c = max(a)
print(c)


# if the list has zero value, min() and max() will return error
# there is another way even the list still in zero to avoid error
def minimum(lst):
    try:
        return min(lst)
    except ValueError:
        print('There is no value in the list')

z = []
print(minimum(z))

print(minimum(a))
