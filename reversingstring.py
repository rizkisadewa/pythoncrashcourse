# Reversing String

# own function
def reverseString(s):
    lstr = list(s)
    i=0 ; j=len(s)-1
    while(i<j):
        temp = lstr[i]
        lstr[i] = lstr[j]
        lstr[j] = temp
        i += 1; j -= 1
    return ''.join(lstr)

print(reverseString('Python'))

'''
join() will merge all the list , example
''.join(['H','E','L','L','O'])
result = HELLO
'''

# another algorithm
def reverseString2(s):
    lstr = list(s)
    lstr.reverse()
    return ''.join(lstr)

print(reverseString2('Informatika'))
