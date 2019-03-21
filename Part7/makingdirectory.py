# Making a directory
import os

# os.mkdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydir")

# checking directy that has been created
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydir"))
print(os.path.isdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydir"))

for name in os.listdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
    if os.path.isdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
        print(name)

'''
if directory exist, the os.mkdir cannot be processed. We can handle with condition
'''

if os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydir") == True:
    print("Directory has already exist, we cannot make the new directory with the same directory name")
else:
    os.mkdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydir")