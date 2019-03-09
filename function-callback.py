# Callback function
def addition(a, b):
    return a + b;

def printout(x):
    print(x)

def multiple(a,b):
    return a * b

# callback function define below
def caller(function, argument_list, *, callback):
    # addition process
    result = function(*argument_list)

    # show the result
    callback(result)

# call the callback function
caller(addition, (10, 20), callback=printout)
caller(multiple, (10, 20), callback=printout)
