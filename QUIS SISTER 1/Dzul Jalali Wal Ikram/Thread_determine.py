import threading
from time import ctime, sleep
from random import randrange


def task1():
    print (threading.currentThread().getName()+str('--> Memulai Tugas'))
    sleep(randrange(2, 5))
    print (threading.currentThread().getName()+str( '--> Tugas Selesai'))
    return

def task2():
    print (threading.currentThread().getName()+str('--> Memulai Tugas'))
    sleep(randrange(2, 5))
    print (threading.currentThread().getName()+str( '--> Tugas Selesai'))
    return

def task3():
    print (threading.currentThread().getName()+str('--> Memulai Tugas'))
    sleep(randrange(2, 5))
    print (threading.currentThread().getName()+str( '--> Tugas Selesai'))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='task1', target=task1)
    t2 = threading.Thread(name='task2', target=task2)
    t3 = threading.Thread(name='task3',target=task3) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
