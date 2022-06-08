from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_cerdascermat = 5
hasilakhir = Barrier(num_cerdascermat)
peserta = ['nisa', 'rama', 'titin', 'budi', 'ani']

def siswa():
    name = peserta.pop()
    sleep(randrange(2, 7))
    print('%s selesai mengerjakan pada: %s \n' % (name, ctime()))
    hasilakhir.wait()

def main():
    threads = []
    print('mulai mengerjakan!!')
    for i in range(num_cerdascermat):
        threads.append(Thread(target=siswa))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('selesai!')

if __name__ == "__main__":
    main()
