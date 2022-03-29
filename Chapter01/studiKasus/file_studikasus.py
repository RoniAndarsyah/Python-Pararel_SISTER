f = open ('file_studikasus.txt', 'w')
nama = input('Masukan Nama Anda :')
alamat = input('Masukan Alamat Anda :')
hobi = input('Masukan Hobi Anda :')
f.write (nama + '\n') 

f.write (alamat + '\n') 
f.write (hobi + '\n')

f.close()
f = open ('file_studikasus.txt') 
content = f.read() 
print (content)

f.close() 
