# Copying Dictionary, we can use copy()
d = {'satu':100, 'dua':200, 'tiga':300}
print(d)
b = d.copy()
print(b)

'''
using copy() will only copy the reference without make any copy, means the two variables above
'''

# another method that we can define , own method
def copydict(d):
    temp = {}
    for key, value in d.items():
        temp[key] = value
    return temp

c = copydict(d)
print(c)
