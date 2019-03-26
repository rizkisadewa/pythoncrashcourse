# Module Dua Dimensi
import math

class persegipanjang:
    def __init__(self, p=0, l=0):
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

    def luas(self):
        return self.__panjang * self.__lebar

    def keliling(self):
        return 2 * (self.__panjang * self.__lebar)

class lingkaran:
    def __init__(self, r=0):
        self.__jarijari = r

    @property
    def jarijari(self):
        return self.__jarijari
    @jarijari.setter
    def jarijari(self, r):
        self.__jarijari = r

    def luas(self):
        return math.pi * pow(self.__jarijari, 2)

    def keliling(self):
        return 2 * math.pi * self.__jarijari