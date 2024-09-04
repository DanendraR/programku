hargakendaraan = {"Avanza": 50000,
                  "Jazz": 60000,
                  "Inova": 100000,
                  "Pajero": 150000}

# Tampilkan daftar mobil yang tersedia
print("Daftar Mobil yang Tersedia:")
for mobil in hargakendaraan:
    print(f"- {mobil} (Rp{hargakendaraan[mobil]})")

# Input pilihan pengguna
pilihan = input("Masukkan nama mobil yang ingin disewa: ")

# Periksa apakah mobil tersedia
if pilihan.lower() in hargakendaraan:
    print(f"Anda menyewa sebuah {pilihan} dengan harga sewa Rp{hargakendaraan[pilihan]}")
else:
    print("Mobil tidak tersedia.")