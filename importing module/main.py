# import myclasses module
import myclasses

def main():
    # make an object from class A
    a = myclasses.A()

    # make an object from class B
    b = myclasses.B()

    # make an object from class C
    c = myclasses.C()

    # calling method in class A, B, and C
    a.method()
    b.method()
    c.method()

if __name__ == '__main__':
    main()