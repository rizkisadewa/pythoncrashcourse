# Deleting Dictionary
d = {'one':100, 'two':200, 'three':300}
print(d)
del d['one']
print(d)

# if we would like to delete some of values in Dictionary, we use a key
d1 = {'one':100, 'two':200, 'three':300, 'four':400, 'five':500, 'six':600}
print(d1)
keys = ['one','two','five'] # keys in list

# delete using looping with refer to keys
for key in keys:
    del d1[key]

print(d1)

# if we would like to delete entire values in Dictionary, use a clear()
d3 = {'one':100, 'two':200, 'three':300, 'four':400, 'five':500, 'six':600}
d3.clear()
print(d3)
print(len(d3))
