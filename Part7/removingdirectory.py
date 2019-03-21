# Removing Directory
import os

# Deleting directory
# os.rmdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydirchanged")
if os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydirechanged") == False:
    print("File has been deleted")

'''
we need to know the different below: 
os.remove(), use for deleting file 
os.rmdir(), use for deleting empty directory
shutil.rmtree(), use for deleting directory which has file/s inside that
'''