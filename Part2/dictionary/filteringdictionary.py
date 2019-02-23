# Filtering Dictionary
d = {'one':100, 'two':101, 'three':102, 'four':103}

genap = {k:v for k,v in d.items() if v % 2 == 0}
print(genap)

'''
k:v is how we can input the key into value from Dictionary
'''
