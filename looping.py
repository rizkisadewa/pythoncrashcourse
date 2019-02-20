#Looping using while 
BARIS = 5
i = 1
while i <= BARIS:
    j = 1
    while j<=i:
        print("%d"%(i*j), end='')
        j += 1 
    print() #ganti baris
    i += 1

#Looping combination with for
BARIS2 = 5
for i in range(1, BARIS2+1):
    j = 1
    while j<=i:
        print("%d"%(i*j), end='')
        j += 1
    print() #ganti baris
    i += 1

BARIS3 = 5
while i <= BARIS3:
    j = 1
    for i in range(1, i+1):
        print("%d"%(i*j), end='')
        j +=  1
    print() #ganti baris
    i += 1
