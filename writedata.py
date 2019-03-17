# Write a Data into file

# make the file
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data1.txt", 'w')

# write the data into the file
# f.write('First row \n')
# f.write('second row \n')
# f.write('Thrid row \n')
# f.write('Fourth row \n')
# f.write('Fifth row \n')

# Write the data into the file option 2
data = [
    'First row option 2 \n',
    'Second row option 2 \n',
    'Third row option 2 \n',
    'Fourth row option 2 \n'
]

# write the data into file
f.writelines(data)

# closing the file
f.close()
