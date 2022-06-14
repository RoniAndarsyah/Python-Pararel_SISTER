from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jmlh_org = 3
kota_tujuan = Barrier(jmlh_org)
orangmudik = ['Asep Gokil', 'Udin Wazowski', 'Papope Cool']

def mudik():
    name = orangmudik.pop()
    sleep(randrange(2, 5)) # Menunggu sesuai waktu antara 2 sampai 5 detik secara random
    print('%s Sampai Ke Kota pada hari: %s \n' % (name, ctime()))
    kota_tujuan.wait() # Menunggu semua thread selesai

def main():
    threads = []
    print('Mudik Dilaksanakan')
    # Membuat Thread
    for i in range(jmlh_org):
        # Membuat thread baru untuk menjalankan function
        threads.append(Thread(target=mudik))
        threads[-1].start()
        # Menunggu semua thread selesai
    for thread in threads:
        thread.join()
    print('Alhamdulillah, sampai ditempat tujuan dengan selamat') # Thread selesai

if __name__ == "__main__":
    main()
