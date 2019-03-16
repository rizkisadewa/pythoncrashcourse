# Abstract Class
from abc import ABCMeta, abstractmethod

# Abstract Class example
class duadimensi(metaclass=ABCMeta):
    '''
        Abstract method
    '''
    @abstractmethod
    def luas(self):
        pass # canot have implementation

# obj = duadimensi() # will return the error as this has been delcared abstract
# make luas persegipanjang class
class persegipanjang(duadimensi):
    def __init__(self, p, l):
        self.__panjang = p
        self.__lebar = l

    @property
    def panjang(self):
        return self.__panjang
    @panjang.setter
    def panjang(self, p):
        self.__panjang = p

    @property
    def lebar(self):
        return self.__lebar
    @lebar.setter
    def lebar(self, l):
        self.__lebar = l

    # Override duadimensi.luas() method
    def luas(self):
        return self.__panjang * self.__lebar

# Make luas segitiga
class segitiga(duadimensi):
    def __init__(self, a, t):
        self.__alas = a
        self.__tinggi = t

    @property
    def alas(self):
        return self.__alas
    @alas.setter
    def alas(self, a):
        self.__alas = a

    @property
    def tinggi(self):
        return self.__tinggi
    @tinggi.setter
    def tinggi(self, t):
        self.__tinggi = t

    # Override duadimensi.luas() method
    def luas(self):
        return self.__alas * self.__tinggi / 2

# Make lingkaran class
class lingkaran(duadimensi):
    def __init__(self, r):
        self.__jarijari = r

    @property
    def jarijari(self):
        return self.__jarijari
    @jarijari.setter
    def jarijari(self, r):
        self.__jarijari = r

    # Override duadimensi.luas() method
    def luas(self):
        import math
        return math.pi * pow(self.__jarijari, 2)

# make an object of persegi panjang
obj = persegipanjang(10, 8)
print(obj.luas())

# Make an object of segitiga
obj2 = segitiga(5, 4)
print(obj2.luas())

# Make an object of lingaran
obj3 = lingkaran(3)
print(obj3.luas())

