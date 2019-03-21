# read data file per line

# open the file
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.txt", 'r')

# # open based on line
# line = f.readline()
# while line:
#     print(line, end='')
#     line = f.readline()

# open based on line option 2
for line in f:
    print(line, end='')

f.close()
