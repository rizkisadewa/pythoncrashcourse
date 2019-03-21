# There are two option to copy the file

# Option 1 : make own function
def copyfile(sourcefile, destfile):
    f1 = open(sourcefile, 'r')  # reading mode
    f2 = open(destfile, 'w')  # writing mode
    for data in f1.read():
        '''
        Writing data to fw 
        '''
        f2.write(data)
    f1.close()
    f2.close()


# # make an object
# copyfile("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data1.txt",
#          "D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\data1.txt")
#
# # checking the file
# import os
# print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\data1.txt"))
'''
The above function cannot copy a zip file
'''

# Option 2 : ushing shutil module
import shutil

# copying file
shutil.copy("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\example.zip",
            "D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\example.zip")
# checking the file
import os
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\example.zip"))

'''
using shutil, we can copy whatever kind of file
'''