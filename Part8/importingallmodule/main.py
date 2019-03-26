# importing all member of modul.py
from importingallmodule.modul import *

def main():
    # showing variable in modul
    print(myvar)

    # calling function in modul
    myfunc()

    # make an object from class A
    # inside modul.py
    a = A()

    # calling mymethod() through object a
    a.mymethod()

if __name__ == '__main__':
    main()

'''
* means all of component imported in this file
'''