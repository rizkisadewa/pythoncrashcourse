# Read All of Line Code
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.txt", 'r')

# read all lines data in the file
data = f.readlines()

# show the data
print(data)
for s in data:
    print(s, end='')

'''
readlines() will return the list
'''
