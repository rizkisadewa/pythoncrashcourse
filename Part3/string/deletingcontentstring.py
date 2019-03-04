# Deleting Some Character Content in String
s = '          Python              '
print(s.strip())

'''
Using strip() is not change the old object, means this is immutable
'''
s1 = s.strip()
#Show the s
print(s)
# show s address
print(id(s))

#call the s1 object
print(s1)
# show s1 addres
print(id(s1))

'''
There are 3 method in str,
1. strip() => is for deleting space in the begining and ending
2. lstrip() => is for deleting space in the beginning only
3. rstrip() => is for deleting space in the ending only
'''
print(s.lstrip())
print(s.rstrip())

'''
We can also deleting the character that content specified
'''
s2 = '**************Python****************'
print(s2)

print(s2.strip('*'))

s3 = 'abcdePYTHONabcde'
print(s3)
print(s3.strip('abcde'))
