from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

lomba = 4
finish_line = Barrier(lomba)
nama_peserta = ['Audry', 'Bella', 'Vino', 'Lala']

def peserta():
    name = nama_peserta.pop()
    sleep(randrange(2, 4))
    print(' %s mulai lomba melukis pada: %s \n' % (name, ctime()))
    finish_line.wait()
    print(' %s selesai melukis pada: %s \n' % (name, ctime()))

def main():
    threads = []
    print('Mulai Lomba Melukis')
    for i in range(lomba):
        threads.append(Thread(target=peserta))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Selesai!')

        
if __name__ == "__main__":
    main()
