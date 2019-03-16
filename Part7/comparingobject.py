# Comparing Class Object

class lingkaran:
    def __init__(self, r):
        self.__jarijari = r

    # overload operator ==
    def __eq__(self, object):
        return self.__jarijari == object.__jarijari

    # overload operator <
    def __lt__(self, object):
        return self.__jarijari < object.__jarijari

    # overload operator <=
    def __le__(self, object):
        return self.__jarijari <= object.__jarijari

    # overload operator >
    def __gt__(self, object):
        return self.__jarijari > object.__jarijari

    # overload operator >=
    def __ge__(self, object):
        return self.__jarijari >= object.__jarijari

    # menghitung luas
    def luas(self):
        import math
        return math.pi * pow(self.__jarijari, 2)

    # menghitung keliling
    def keliling(self):
        import math
        return 2 * math.pi * self.__jarijari

# an object
obj1 = lingkaran(3)
obj2 = lingkaran(5)
obj3 = lingkaran(3)

# comparing object
print(obj1 == obj2)
print(obj1 == obj3)
print(obj1 < obj2)
print(obj2 > obj3)
print(obj1 >= obj3)

