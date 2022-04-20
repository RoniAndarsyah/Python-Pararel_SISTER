from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_mhs = 3 
b = Barrier(num_mhs) 
mhs = ['Ahmad', 'Alwi', 'Abdul']

# barrier = barrier digunakan untuk memblock semua thread,kemudian melepas semua untuk execute secara bersamaan

def runner():
    name = mhs.pop()
    sleep(randrange(2, 10))
    print('%s Berangkat kuliah pada: %s ' % (name, ctime()))
    b.wait()
    print('%s Pulang kuliah pada: %s ' % (name, ctime()))

def main():
    threads = []
    print('Gas kuliah!!!!')
    for i in range(num_mhs):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Udah pada balik!')

if __name__ == "__main__":
    main()