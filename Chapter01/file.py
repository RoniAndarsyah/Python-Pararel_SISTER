f = open ('test.txt', 'w') #menulis dalam format text.
f.write ('first line of file \n') #menulis string didalam file yang telah dibuka

f.write ('second line of file \n') #menulis string didalam file yang telah dibuka

f.close() #menutup file
f = open ('test.txt') #membuka file pada direktori saat ini untuk dibaca
content = f.read() #membaca string dari file
print (content) #menampilkan konten yang ada didalam file

f.close() #menutup file


