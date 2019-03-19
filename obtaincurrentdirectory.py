# Obtain Current Working Directory
import os
print(os.curdir) # checking tentative current directory
print(os.path.abspath(os.curdir)) # checking absolute directory

# try to change the directory
os.chdir("D:\Rizky's File\Abimanyu")
print(os.curdir) # checking tentative current directory
print(os.path.abspath(os.curdir)) # checking absolute directory
