# Data Static
class circle:
    PI = 3.14 # data static

    def __init__(self, r):
        self.__jarijari = r

    @property
    def jarijari(self):
        return self.__jarijari
    @jarijari.setter
    def jarijari(self, r):
        self.__jarijari = r

    def luas(self):
        return PI * pow(self.__jarijari, 2)

    def keliling(self):
        return 2 * PI * self.__jarijari

obj1 = circle(3)
obj2 = circle(5)
obj3 = circle(7)

print(circle.PI)
print(obj1.PI)
print(obj2.PI)
print(obj3.PI)

# Change the value in circle.PI
import math
circle.PI = math.pi
print(circle.PI)
print(obj1.PI)
print(obj2.PI)
print(obj3.PI)

'''
PI is belong to the circle class
'''