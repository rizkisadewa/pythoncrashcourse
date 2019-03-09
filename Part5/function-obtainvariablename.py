# Obtain Variable Name in String
def varname(obj, namespace):
    temp = [k for k in namespace if namespace[k] is obj]
    if len(temp) > 0:
        return temp[0]

# Implementation
myvar = 13
print(varname(myvar, globals()))

print(globals()['myvar'])
print(myvar)

s = 'Python'
print(varname(s, globals()))

'''
the result of the searching will be gotten from global dictionary, to get the global dictionary we can use
globals() as the python built function
'''
