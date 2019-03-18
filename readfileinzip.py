# Read the file in zip file
import zipfile

readzf = zipfile.ZipFile("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\example.zip", 'r')

# showing the files inside of zip file
for filename in readzf.namelist():
    print(filename)