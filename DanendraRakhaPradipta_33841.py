#Daftar harga dan kendaraan yang tersedia
hargakendaraan = {"Avanza":50000,
                  "Jazz":60000,
                  "Inova":100000,
                  "Pajero":150000 }
#list mobil
print("List Mobil yang Tersedia")
for list in hargakendaraan:
    print(f"-> {list} RP{hargakendaraan[list]}/malam")

#isi input kendaraan yang diinginkan
pilihan = input("Mobil yang ingin disewa : ")
#kondisi perulangan
if pilihan in hargakendaraan:
    print(f"Anda menyewa sebuah {pilihan} dengan nominal {hargakendaraan[pilihan]} ")
else:
    print("tidak terdaftar")