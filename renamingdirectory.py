# Rename Directory
import os

# Change the name of directory
os.rename("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydirechanged", "D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydirchanged")
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\mydirchanged"))

'''
if we have already changed the directory with the above script, we cannot do twice and the system will return error. 
to do that we can handle with conditional
'''