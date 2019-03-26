# importing mymodule
from mymodule import *

def main():
    # showing variable in mymodule
    print(var1)
    print(var2)

    # calling function
    f1()
    f2()

    # Make an object from c1 and c2 class
    a = c1()
    b = c2()

    # calling method m() melalui object a dan b
    a.m()
    b.m()

if __name__ == '__main__':
    main()