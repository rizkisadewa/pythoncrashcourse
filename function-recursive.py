# Recursive Function
def factorial(n):
    if n == 0: return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

'''
means we call function in that own function
'''
