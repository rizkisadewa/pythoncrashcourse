# Making File CSV
import csv

data = [(1, "Dennis Ritchie", "C"),
        (2, "Bjarne Stroustroup", "C++"),
        (3, "James Gosling", "Java"),
        (4, "Larry Wall", "Perl"),
        (5, "Guido Van Rossum", "Python"),
        (6, "Yukihiro Matsumoto", "Ruby")]

# Make the file of CSV
with open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\pencipta.csv", 'w', newline='', encoding='utf-8') as csvfile:
    '''
    Writing the data to CSV file 
    '''
    w = csv.writer(csvfile, delimiter=',')
    w.writerows(data)
    csvfile.close()

# Checking File Existance
import os
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\pencipta.csv"))
