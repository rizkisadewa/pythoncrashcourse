# importing modul bangun_dua_dimensi
# using alias duaD
import bangun_dua_dimensi as duaD

def main():
    # making an object from persegipanjang
    a = duaD.persegipanjang()
    a.panjang = 10
    a.lebar = 8

    # make an object from lingaran class
    b = duaD.lingkaran()
    b.jarijari = 4

    # calling method in persegipanjang class and lingkaran class
    print("PERSEGI PANJANG")
    print("LUAS : %0.1f"% a.luas())
    print("KELILING : %0.1f"% a.keliling())

    print("\nKELILING")
    print("LUAS : %0.1f"% b.luas())
    print("KELILING : %0.1f"% b.keliling())

if __name__ == '__main__':
    main()