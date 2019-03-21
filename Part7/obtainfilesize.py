# Obtaining File Size
import os
print(os.path.getsize(format('%s\%s'% ("D:\Rizky's File", "test.py"))))

names = os.listdir("D:\Rizky's File")

for name in names:
    print(name, end='')
    if os.path.isdir("D:\Rizky's File\%s" % name) == True:
        print('\t\t\t[DIR]')
    else:
        import math
        size = math.ceil(os.path.getsize(format('%s\%s'% ("D:\Rizky's File", name))) / 1024)
        if len(name) <= 1:
            print('\t', end='')
        else:
            print('\t\t\t', end='')
        print('%3d KB'% size)