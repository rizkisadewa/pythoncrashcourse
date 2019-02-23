# Extracting Dictionary
def extractdict(d, keys):
    temp = {}
    for key in keys:
        temp[key] = d[key]
    return temp

d = {'one':100, 'two':200, 'three':300}
print(d)

b = extractdict(d, ['one','two'])
print(b)

c = extractdict(d, ['three'])
print(c)

'''
The extractict will make a new dictionary as per parameter keys refer to the dictionary in parameter d
'''
