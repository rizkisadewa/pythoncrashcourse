# Class 
class Segiempat:
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

obj = Segiempat(8, 6)
luas = obj.luas()
print(luas)
keliling = obj.keliling()
print(keliling)
