# Mendefinisikan variabel boolean
is_sunny = True
is_weekend = False

# Menggunakan tipe data boolean dalam percabangan
if is_sunny:
    print("Hari ini cerah!")
else:
    print("Hari ini mendung.")

if is_sunny and is_weekend:
    print("Saatnya jalan-jalan!")
elif is_sunny and not is_weekend:
    print("Hari kerja, tapi cuaca bagus.")
else:
    print("Cuaca kurang mendukung.")

# Menggunakan boolean sebagai hasil dari operasi perbandingan
age = 20
is_adult = age >= 18  # Hasilnya akan True jika umur >= 18
print("Apakah sudah dewasa?", is_adult)
