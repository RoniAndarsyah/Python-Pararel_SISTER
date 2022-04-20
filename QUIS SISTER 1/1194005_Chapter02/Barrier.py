from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

lomba = 4
finish_line = Barrier(lomba)
nama_peserta = ['Artha', 'Glory', 'Romey']

def peserta():
    name = nama_peserta.pop()
    sleep(randrange(2, 4))
    print(' %s mulai olahraga pada: %s \n' % (name, ctime()))
    finish_line.wait()
    print(' %s selesai olahraga pada: %s \n' % (name, ctime()))

def main():
    threads = []
    print('Mulai olahraga ')
    for i in range(lomba):
        threads.append(Thread(target=peserta))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Selesai Olahraga!')

        
if __name__ == "__main__":
    main()