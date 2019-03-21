# Making JSON file
import json
import os

# a data that will be written in json file
data = {
    'employee': [
        {'NIP':'1001', 'name':'Anis Yuliana Phasya', 'salary':6000000},
        {'NIP':'1002', 'name':'Rizki Sadewa', 'salary':120000000},
        {'NIP':'1003', 'name':'Abimanyu', 'salary':8000000}
    ]
}

# change the dictionary above to string with json format
json_str = json.dumps(data)
print(json_str)

# making JSON file
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.json", 'w')
f.writelines(json_str)
f.close()

# checking file existance of JSON
print(os.path.exists("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.json"))