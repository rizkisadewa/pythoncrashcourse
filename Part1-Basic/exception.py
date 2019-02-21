# KASUS 1: terjadi kesalahan pada saat pengambilan index list
data = [10,20,30]
try:
    x = data[3]
except:
    print("Tidak ada index ke-3 di dalam list data")
else:
    print("Nilai x adalah %d" % x)

# KASUS 2: tidak terjadi kesalahan pada saat pengambilan index list
data = [10,20,30, 40]
try:
    x = data[3]
except:
    print("Tidak ada index ke-3 di dalam list data")
else:
    print("Nilai x adalah %d" % x)

# Blok try-finally
# KASUS 1: terjadi kesalahan pada saat pengambilan index list
data = [10,20,30]
try:
    x = data[3]
except:
    print("Tidak ada index ke-3 di dalam list data")
else:
    print("Nilai x adalah %d" % x)
finally:
    print('Bagian finalisasi dipanggil ....')

# KASUS 2: tidak terjadi kesalahan pada saat pengambilan index list
data = [10,20,30, 40]
try:
    x = data[3]
except:
    print("Tidak ada index ke-3 di dalam list data")
else:
    print("Nilai x adalah %d" % x)
finally:
    print('Bagian finalisasi dipanggil ....')
