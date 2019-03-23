# mengimport module
import packagesquance.bangun2d.persegipanjang
import packagesquance.bangun2d.lingkaran
import packagesquance.bangun3d.tabung
import packagesquance.bangun3d.balok

def main():
    a = packagesquance.bangun2d.persegipanjang.luas(10, 8)
    b = packagesquance.bangun2d.persegipanjang.keliling(10, 8)
    c = packagesquance.bangun2d.lingkaran.luas(3)
    d = packagesquance.bangun2d.lingkaran.keliling(3)
    e = packagesquance.bangun3d.balok.volume(3, 8, 4)
    f = packagesquance.bangun3d.tabung.volume(8,4)

    # menampilkan nilai dari variable - variable
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

if __name__ == '__main__':
    main()