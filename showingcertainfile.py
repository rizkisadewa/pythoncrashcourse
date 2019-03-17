# Showing Certain File

def listfile(path, extension):
    temp = []
    import os
    names = os.listdir(path)
    for name in names:
        if name.endswith(extension):
            temp.append(name)
    return temp

# use the function of listfile()
files = listfile("D:\Rizky's File", '.py')
print(files)