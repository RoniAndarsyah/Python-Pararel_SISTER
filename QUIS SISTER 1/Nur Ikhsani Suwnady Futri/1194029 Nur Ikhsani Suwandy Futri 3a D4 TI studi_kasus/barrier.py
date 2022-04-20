#studi kasus tentang perlombaan cerdas cermat
from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_cerdascermat = 5
hasilakhir = Barrier(num_cerdascermat)
peserta = ['nisa', 'rama', 'titin', 'nur', 'ayu']

def siswa():
    name = peserta.pop()
    sleep(randrange(2, 7)) # menunggu dengan sesuai waktu dari 2 samap denga 7 secara random
    print('%s selesai mengerjakan pada: %s \n' % (name, ctime()))
    hasilakhir.wait() #menunggu semua thread selesai digunakan untuk memblokir 
    #thread yang melakukan panggilan

def main():
    threads = []
    print('mulai mengerjakan!!')
    for i in range(num_cerdascermat): #membuat tread baru agar dapar menjalankan function
        threads.append(Thread(target=siswa))
        threads[-1].start() #menunggu thread selesai
    for thread in threads:
        thread.join()
    print('selesai!')#tread selesai

if __name__ == "__main__":
    main()
