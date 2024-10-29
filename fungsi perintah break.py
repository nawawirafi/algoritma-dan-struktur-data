#Berikut format dasar penggunaan perintah break dalam perulangan while:
# start;
# while condition1:
  # kode program yang akan diulang
  # kode program yang akan diulang
#  if condition2:
#    break
#  increment

#Contoh Kode Program Perintah break Python
#Sebelum masuk ke perintah break, berikut contoh perulangan while Python untuk 
#menampilkan daftar perkalian angka:

a = 3
while a <= 10:
  print(a,' x ',a ,' = ',a*a)
  a += 3

#Sekarang saya ingin jika variabel counter b sudah mencapai angka 20, maka 
#hentikan perulangan (break). Berikut kode programnya:

b = 1
while b <= 40:
  print(b,' x ',b ,' = ',b*b)
  if b == 20:
    break
  b += 1

#Sebagai penutup, berikut contoh penggunaan perintah break pada perulangan for Python:

for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break