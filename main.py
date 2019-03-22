# importing module1.py and module2.py inside of package1
import package1.module1, package1.module2

def main():
    a = package1.module1.additional(4, 3)
    b = package1.module1.reduction(4, 3)
    c = package1.module2.multiple(4, 3)
    d = package1.module2.fraction(4, 3)

    # showing the value from the variables above
    print(a)
    print(b)
    print(c)
    print(d)

if __name__ == '__main__':
    main()