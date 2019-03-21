# Reading JSON file
import json

# open the JSON file
f = open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.json", 'r')

# reading and put into string
# Option 1
json_str = ''.join(f.readlines())
f.close()
print(json_str)
print(type(json_str)) # proof that json_str is a string

# Option 2
# with open("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse\data.json", 'r') as f:
#     data = json.load(f)
#     f.close()

# convert string to JSON format and put in an object
data = json.loads(json_str)
print(data)
print(type(data))

'''
readlines() : will return a list format, to conver list to string format, then we need to have join() which is ''.join(f.readlines())
if we would not like to have string format in the begining, ten we need to use load() not loads, example in option 2 above
'''