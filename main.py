# importing myvar variable and calss A in modul.py
from modul import myvar, A

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