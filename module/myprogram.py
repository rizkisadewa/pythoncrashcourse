# The Program will execute the module in file mymodule.py
from importanddivide import mymodule as m


def main():
    print('Nilai A adalah %d' % m.a)
    print('2 + 3 = %d' % m.tambah(2, 3))
    print('2 x 3 = %d' % m.kali(2, 3))

if __name__ == '__main__':
    main()
