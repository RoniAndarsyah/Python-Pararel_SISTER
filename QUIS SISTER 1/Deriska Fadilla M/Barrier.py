from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_absensi = 3
hasilakhir = Barrier(num_absensi)
nama = ['deriska', 'nur', 'ayu']

def mahasiswa():
    name = nama.pop()
    sleep(randrange(1, 5))
    print('%s input absen pada: %s \n' % (name, ctime()))
    hasilakhir.wait()

def main():
    threads = []
    print('mulai berangkat!!')
    for i in range(num_absensi):
        threads.append(Thread(target=mahasiswa))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('berhasil absen!')

if __name__ == "__main__":
    main()
