# Simple Array
import array
a = array.array('i', [10,20,30,40,50])
print(a[0])

'''
i means the above is integer, below the code that we use

Type code = C type = Python type = Size
b = char = int = 1 byte
B = unassigned char = int = 1 byte
u = unicode char = unicode = 2 byte
h = short = int = 2 byte
H = unassigned short = int = 2 byte
i = int = int = 2 byte
I = unassigned = long = 2 byte
l = long = int = float = 4 byte
L = unassigned long = long = 4 byte
f = float = float = 4 byte
d = double = float = 4 byte
'''

# Adding Array element
a.append(60)
a.append(70)
print(a)

# or we can add the element using insert
a.insert(2, 88)
print(a)
'''
2 means we insert 88 in index number 2
'''

# if we would like to add the element more than one
a.extend([30,30,30,30])
print(a)

# Editting the element
a[0] = 90
a[1] = 90
print(a)

'''
remember : the array is immutable, means nonchangeable.
a[0] = 90 will directed to new memory which is has address 90
the original object will be removed by Python internal system
'''

# Deleting Python
a.remove(30)
print(a)
'''
the remove() will be deleting one of element.
if we would like to delete the last element, we can use pop()
'''

x = a.pop()
print(x)
print(a)
'''
pop() is like we pick the last element. x = a.pop() means we pick the last element then assign to x variable
'''

# sorting element of array
def sortarray(a):
    for i in range(0, len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                # switch array element
                a[j], a[j-1] = a[j-1], a[j]

'''
the above method will compare the last element value with lower index
'''

# implement of the sortarray method
sortarray(a)
print(a)

# reversing the array element
b = array.array('u', ['n','o','h','t','y','P'])
for i in b:
    print(i, ' ', end='')

print() # \n

b.reverse() # reversing the array
for i in b:
    print(i, ' ', end='')

print() # \n

# Array constant
BULAN = ('January', 'February','March','April','May','June','July','August','September','October','November','December')
print(BULAN[0])

# Array two dimension
twoD = [
    ['P001','Pencil'],
    ['P002','Book'],
    ['P003','Bag']
]

print(twoD[0][0])
print(twoD[0][1])
print(twoD[1][0])
print(twoD[1][1])
print(twoD[2][0])
print(twoD[2][1])

'''
array in python is only can handle for one dimension, however we can use list to declare the array with two dimension or more dimension
'''
