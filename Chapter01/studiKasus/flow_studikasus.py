nilai = int(input('Masukan Nilai Ujian Anda : '))
if nilai >= 75:
    print("Selamat Anda Lolos")
elif nilai == 0:
    print("Anda Tidak Ikut Ujian")
else:
    print("Anda Ikut Remedial")


# FOR
durasi_kerja = float(input('masukan durasi kerja: '))

if durasi_kerja > 8:
    print("Durasi Kerja + Lembur")
elif durasi_kerja == 8:
    print("Durasi Kerja Rata-rata")
else:
    print("Durasi Kerja Dibawah Rata-Rata")

 
############1
total_durasi_kerja = [7,8,9]

durasi_lembur = 4
for val in total_durasi_kerja:
    durasi_lembur = durasi_lembur+val

print("Total Semua Durasi Kerja", durasi_lembur)

if durasi_lembur > 12.00:
    print("CAPEK")
elif durasi_lembur == 0.00:
    print("Anda Kerja ?")
else:
    print("Kerja Santai")


#WHILE
# Program to add natural numbers upto sum = 1+2+3+...+n

n = 10
# initialize sum and counter
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)