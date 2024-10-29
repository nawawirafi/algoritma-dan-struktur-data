#Pengertian Perintah Continue dalam Python
#Perintah continue mirip seperti perintah break, hanya saja jika dalam perintah 
#break perulangan langsung berhenti, untuk perintah continue perulangan hanya melewati 
#1 kali proses iterasi saja.

#Berikut format dasar penggunaan perintah continue dalam perulangan for Python:
# for i in range(1,x): 
#  if condition2: 
#    continue
  # kode program yang akan diulang 
  # kode program yang akan diulang

#Sebelum masuk ke perintah continue, berikut contoh perulangan for Python untuk 
#menampilkan daftar perkalian angka:
for a in range(1,12):
  print(a,' x ',a ,' = ',a*a)

#Sekarang kita akan tambah dengan perintah continue:
for b in range(1,12):
  if b == 5:
    continue
  print(b,' x ',b ,' = ',b*b)

#Sebagai tambahan, berikut contoh kode program perintah continue dalam perulangan while:
c = 0
while c < 10:
  c += 1
  if c == 5:
    continue
  print(c,' x ',c ,' = ',c*c)