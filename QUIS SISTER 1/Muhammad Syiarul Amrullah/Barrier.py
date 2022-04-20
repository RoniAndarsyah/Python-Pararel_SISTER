from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_masakan = 3
finish_line = Barrier(num_masakan)
list_masakan = ['mie ayam', 'mie goreng', 'nasi goreng']

def masakan():
    name = list_masakan.pop()
    sleep(randrange(2, 5))
    print('%s selesai dimasak pada: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('START Cook!!!!')
    for i in range(num_masakan):
        threads.append(Thread(target=masakan))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Cook over!')

if __name__ == "__main__":
    main()
