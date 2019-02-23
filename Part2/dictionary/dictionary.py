# Dictionary
a = {1:100, 2:200, 3:300, 4:400, 5:500}
print(a[1])
print(a.get(2))
'''
Dictionary index will be started from 1
'''

d = {'satu':100, 'dua':200, 'tiga':300, 'four':400}
print(d['satu'])
print(d['dua'])

# We can also call a key list that contain in Dictionary with using keys() and value using values()
print(d.keys())
print(d.values())

# Or using own methods
def getkeys(d, value):
    temp = []
    for key in d:
        if d[key] == value:
            temp.append(key)
    return temp

d1 = {1:100, 2:200, 3:300, 4:400, 5:500}
print(getkeys(d1, 300))

d2 = {1:100, 2:200, 3:300, 4:400, 5:500}
print(getkeys(d2, 300))
