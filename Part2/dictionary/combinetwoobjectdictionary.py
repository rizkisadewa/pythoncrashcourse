# Combine Two Dictionary
def combinedict(d1, d2):
    for k,v in d2.items():
        d1[k] = v
    return d1

d1 = {'one':100, 'two':101, 'three':102}
d2 = {'four':400, 'five':500}

hasil = combinedict(d1, d2)
print(hasil)
