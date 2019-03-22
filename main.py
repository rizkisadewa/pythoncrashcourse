import os # for chdir function
os.chdir("D:\Rizky's File\Tutorial\Coding\Python\CrashCourse")

# importing module.py
import module

# call function suhuruangan
print(module.suhuruangan())

'''
in IDLE , the above code will not update if there is amendment in module.py due to the IDLE will not read from line 1.
therefore we need to do syntax below

import importlib
importlib.reload(module)

Therefore any change in module.py, the IDLE will recognize
'''