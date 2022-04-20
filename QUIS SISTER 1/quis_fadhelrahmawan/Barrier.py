from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Ragil kuncoro', 'dimana', 'Alamat rumahmu']

def runner():
    name = runners.pop()
    sleep(randrange(3, 10))
    print('%s reached the barrier at: %s \n' % (name, ctime()))#
    finish_line.wait()

def main():
    threads = []
    print('Ayo Pergi jalan sama aku?!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Ayo berangkat!')

if __name__ == "__main__":
    main()
