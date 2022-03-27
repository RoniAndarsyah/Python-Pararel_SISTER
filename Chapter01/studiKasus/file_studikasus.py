f = open ('file_studikasus.txt', 'w') #menulis dalam format text.
nama = input('Masukan Nama Anda :')
alamat = input('Masukan Alamat Anda :')
hobi = input('Masukan Hobi Anda :')
f.write (nama + '\n') #menulis string didalam file yang telah dibuka

f.write (alamat + '\n') #menulis string didalam file yang telah dibuka
f.write (hobi + '\n')

f.close() #menutup file
f = open ('file_studikasus.txt') #membuka file pada direktori saat ini untuk dibaca
content = f.read() #membaca string dari file
print (content) #menampilkan konten yang ada didalam file

f.close() #menutup file
