#Pengertian Named Parameter / Keyword Arguments
#Named parameter adalah istilah programming untuk menyebut cara pengiriman nilai dari 
#argumen ke parameter function dengan menulis nama parameter, tidak sekedar nilainya saja.
#Named parameter ini sering juga disebut sebagai named argument atau keyword argument.

#Berikut format dasar penggunaannya:
# def foo(var1, var2, var3):
  ## isi fungsi disini...
  ## isi fungsi disini...
 
# foo(var3 = 100, var1 = 200, var2 = 300)

#Contoh Kode Program Python untuk Named Parameter:

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil; 
print( pangkat(2) )      
print( pangkat(3,4) )    
print( pangkat(5,6) )    

#Dengan memakai teknik named parameter, kita bisa menjalankan fungsi pangkat() 
#sebagai berikut:

def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
print( pangkat(angka = 1,pangkat = 2) )     
print( pangkat(pangkat = 3,angka = 4) )     

#Sebagai contoh lain, perhatikan fungsi akses_database() berikut ini:

def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database("prezekc","zekc","123456")