# Adding Zero in front of String using zfill()
x = 9
s = str(x) # convert from int to string
print(s.zfill(2))
print(s.zfill(3))
print(s.zfill(4))

'''
Prototype:
S.zfill(width) -> str
widht means we only set up the howmany digit or character that we will be showed
'''

for i in range(1, 16):
    s = str(i)
    print(s.zfill(3))


print('9'.zfill(5))
print('77'.zfill(5))
print('888'.zfill(5))
print('1234'.zfill(5))
