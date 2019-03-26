# importing myvar variable and calss A in modul.py
from importingcertainmodule.modul import myvar, A

def main():
    # showing variable in modul
    print(myvar)

    # myfunc() # will not recognised as we do not import the component in modul.py

    # make an object from class A
    a = A()

    # calling method
    a.mymethod()

if __name__ == '__main__':
    main()

'''
Myfunc() will not recognized as we do not import the function in modul.py, we only import myvar and A class
'''