# Extracting List

# when we have a list less value, then we will store each value into the variablesself.
karyawan = ['KAR-01','Bayu Aji',15000000]
nip, nama, gaji = karyawan
print("Nip : "+nip)
print("Nama : "+nama)
print("Gaji : ",gaji)

print("**********************")

karyawan2 = ['KAR-01','Bayu Aji','L','082144534828',15000000]
nip, nama, *datalain = karyawan2
print("Nip : "+nip)
print("Nama : "+nama)
print("Data Lain : %s"% datalain)

print("**********************")

karyawan3 = ['KAR-01','Bayu Aji','L','082144534828',15000000]
nip, *datalain, gaji= karyawan2
print("Nip : "+nip)
print("Data Lain : %s"% datalain)
print("Gaji : ",gaji)
