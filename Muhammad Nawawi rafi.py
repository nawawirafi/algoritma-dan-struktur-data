string = "hello word"
print (string) 
# Contoh mendefinisikan string
teks1 = "Hello, dunia!"
teks2 = "Belajar Python itu menyenangkan."

# Menggabungkan dua string
gabungan = teks1 + " " + teks2
print("Hasil penggabungan:", gabungan)

# Mengakses karakter pada string
print("Karakter pertama dari teks1:", teks1[0])

# Mengambil sebagian string (slicing)
potongan = teks2[8:14]
print("Hasil slicing:", potongan)

# Menghitung panjang string
panjang_teks = len(teks2)
print("Panjang teks2:", panjang_teks)

# Mengubah string menjadi huruf besar dan huruf kecil
print("teks1 dalam huruf besar:", teks1.upper())
print("teks2 dalam huruf kecil:", teks2.lower())

# Mengecek keberadaan kata dalam string
kata = "Python"
cek = kata in teks2
print(f"Apakah '{kata}' ada di teks2?", cek)

# Menghapus spasi di awal dan akhir string
teks3 = "   Python Programming   "
print("Teks setelah strip:", teks3.strip())

# Mengganti bagian dari string
teks4 = teks2.replace("menyenangkan", "mudah")
print("teks2 setelah replace:", teks4)
