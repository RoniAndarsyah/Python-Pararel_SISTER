from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_QuisDadakan = 5
hasilakhir = Barrier(num_QuisDadakan)
peserta = ['eni', 'eris', 'nazhim', 'helmi', 'siti']

def siswa():
    name = peserta.pop()
    sleep(randrange(2, 7))
    print('%s selesai mengerjakan pada: %s \n' % (name, ctime()))
    hasilakhir.wait()

def main():
    threads = []
    print('mulai mengerjakan!!')
    for i in range(num_QuisDadakan):
        threads.append(Thread(target=siswa))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('selesai!')

if __name__ == "__main__":
    main()
