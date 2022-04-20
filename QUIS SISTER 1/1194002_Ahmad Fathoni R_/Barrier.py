#%%barrier = 3 thread akan nge print dalam waktu yang beda, tapi pas wait->bakal print bareng
# barrier akan menunggu thread lain untuk beres execute 

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_sleepers = 3
finish_line = Barrier(num_sleepers)
sleepers = ['Ahmad', 'Alwi', 'Abdul']

def sleeper():
    name = sleepers.pop()
    sleep(randrange(1, 8))
    print('%s mulai tidur pada: %s ' % (name, ctime()))
    finish_line.wait()
    print('%s Bangun pada: %s ' % (name, ctime()))

def main():
    threads = []
    print('Selamat Tidur')
    for i in range(num_sleepers):
        threads.append(Thread(target=sleeper))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Saatnya sahur')

if __name__ == "__main__":
    main()

#%%barrier = 3 thread akan nge print dalam waktu yang beda, tapi pas wait->bakal print bareng
# barrier akan menunggu thread lain untuk beres execute 

# import time
# import random
# import threading

# def f(b):
#     time.sleep(random.randint(2, 10)) #
#     print("{} execute ketika: {}".format(threading.current_thread().getName(), time.ctime()))
#     b.wait() # akan wait thread lain untuk beres print
#     print("{} keluar dari: {}".format(threading.current_thread().getName(), time.ctime()))

# barrier = threading.Barrier(3)
# for i in range(3):
#     t = threading.Thread(target=f, args=(barrier,))
#     t.start()
# %%