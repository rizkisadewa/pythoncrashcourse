# Global Variabl

gvar = 13

def test():
    global gvar # global variable declaration
    gvar = 8 # asign the value of global variable
    print('Our global variable is : ', gvar)

print(test())
print(gvar)

# Local and Global Variable
gvar2 = 13

def test2():
    gvar2 = 8
    print('This is actually we access local variable which is has been asigned to another value : ', gvar2)

print(test2())
print(gvar2)

'''
We need to declare global if we would like to specify or use the global variable
'''
