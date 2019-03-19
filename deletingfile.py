# Removing the file
import os

# list of file in D:\Rizky's File\Tutorial\Coding\Python\CrashCourse before removed
print("before removed : ")
for name in os.listdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
    if os.path.isfile(name):
        print(name)

os.remove("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\datarubah.txt")

# of file in D:\Rizky's File\Tutorial\Coding\Python\CrashCourse after removed
print("after removed : ")
for name in os.listdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
    if os.path.isfile(name):
        print(name)
