masuk=int(input("Masukkan Jam Masuk = "))
keluar=int(input("Masukkan Jam Keluar ="))
lama=keluar-masuk
payment=12000
print("Lama Mengajar = ", lama, "jam")
if lama <=1:
    satu_jam_pertama=payment
    print("Biaya Mengajar= Rp", satu_jam_pertama)
elif lama <10:
    biaya_selanjutnya = (lama+1)*3000+payment
    print("Biaya Mengajar =  Rp", biaya_selanjutnya)
elif lama >= 10:
    print("Biaya Mengajar =  Rp", 1000000)
else:
    print("nul")
    