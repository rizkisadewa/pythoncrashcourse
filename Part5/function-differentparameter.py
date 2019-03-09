# Different Parameter
def addition(*value):
    total = 0
    for i in value:
        total += 1
    return total

print(addition(1,2))
print(addition(1,3,4))

'''
* or asterisk will be make the parameter as a tuple object. Tuple element will be going through when the function called
'''

# Example 1
def test(*value):
    print(value)

print(test()) # will make empty tuple
print(test(10,20)) # will make the tuple with two element

# Example 2
def myprint(*args):
    for i in args:
        print(str(i), end='')
    print() # make a new line

# implement of Example 2 function
language = 'Python'
myprint('Programming of ', language)

x = 10
y = 20
myprint('Nilai X : ', x, ' Nilai Y: ', y)
