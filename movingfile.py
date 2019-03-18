# Moving File
import shutil

shutil.move("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\move.txt", "D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\move.txt")

# checking file
import os
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\Part5\move.txt"))