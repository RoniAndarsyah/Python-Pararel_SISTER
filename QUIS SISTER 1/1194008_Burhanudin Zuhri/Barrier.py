from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jml_turis = 3
destinasi = Barrier(jml_turis)
nama_turis = ['Andi', 'Budi', 'Caca']

def wisata():
    name = nama_turis.pop()
    sleep(randrange(2, 5))
    print('%s Berangkat sekolah pada hari: %s ' % (name, ctime()))
    destinasi.wait()

def main():
    threads = []
    print('Perjalanan Dimulai')
    for i in range(jml_turis):
        threads.append(Thread(target=wisata))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Semuanya sampai di sekolah tepat waktu')

if __name__ == "__main__":
    main()
