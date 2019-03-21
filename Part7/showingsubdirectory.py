# Showing Sub Directory
import os

print(os.listdir("D:\Rizky's File"))

filenames = os.listdir("D:\Rizky's File")
for filename in filenames:
    print(filename, end='')
    if os.path.isdir("D:\Rizky's File\%s" % filename) == True:
        print('\t\t\t[DIR]')
    else:
        print('\t\t[FILE]')

