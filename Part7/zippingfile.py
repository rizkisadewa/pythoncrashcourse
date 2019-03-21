# Zipping File
import os

# activating directory
os.chdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse")

# choosing the file that would be included in the zip
files = ['data.txt', 'obtainfilesize.py', 'readdataline.py']

# making file .zip
import zipfile
zf = zipfile.ZipFile("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\example.zip", 'w', compression=zipfile.ZIP_DEFLATED)

# Put into the zip file
for file in files:
    zf.write(file)

# closing the file .zip
zf.close()

# checking the file .zip existance
os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\example.zip")
