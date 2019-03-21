# Reading CSV file
import csv

with open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\pencipta.csv", 'r', newline='', encoding='utf-8') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        for i in range(len(row)):
            print('%s\t'% row[i], end='')
        print() # new line
    csvfile.close()