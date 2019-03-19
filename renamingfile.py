# Rename File
import os

# file list in directory : D:\Rizky's File\Tutorial\Coding\Python\CrashCourse before rename
print("Before changing the name : ")
for name in os.listdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
    if os.path.isfile(name):
        print(name)

# change the name
os.rename("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.txt", "D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\datarubah.txt")

print()

# file list in directory : D:\Rizky's File\Tutorial\Coding\Python\CrashCourse after rename
print("AFter changing the name : ")
for name in os.listdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse"):
    if os.path.isfile(name):
        print(name)