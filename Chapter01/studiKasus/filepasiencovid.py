#melakukan percobaan mengimplementasi Input pada file
f = open ('inputPasienCovid.txt', 'w') #membaca file di luar
nik = input ("Masukan NIK :")
nama = input("Masukan Nama : ")
alamat = input("Masukan Alamat : ")
umur = input("Masukan Usia : ")
jeniskelamin = input("Masukan Jenis Kelamin: ")
nohp = input("Masukan Nohp : ")
gejala = input("Masukan Gejala : ")
f.write ("NIK : " + nik + "\n") #menulis ke dalam file
f.write ("Nama : " + nama + "\n") 
f.write ("Alamat : " + alamat + "\n")
f.write ("Umur : " + umur + "\n")
f.write ("Jenis Kelamin : " + jeniskelamin + "\n")
f.write ("No Hp : " + nohp + "\n")
f.write ("Gejala : " + gejala + "\n")
f.close()#keluarkan file nya
f = open ('inputPasienCovid.txt') #buka file
content = f.read()
print (content) #render content yang ada di dalam file nya

f.close()
