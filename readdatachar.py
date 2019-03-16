# Read Data Character in File
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.txt", 'r')

# read per character
# character = f.read()
# while character:
#     print(character, end='')
#     character = f.read()

# read per character option 2, simpler
for character in f.read():
    print(character, end='')

# close the file
f.close()
