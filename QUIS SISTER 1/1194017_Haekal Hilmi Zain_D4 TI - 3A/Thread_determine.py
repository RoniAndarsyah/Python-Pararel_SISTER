import threading
import time
from random import randint


def loop_count():
    loop_count = randint(1, 20)
    print('Memulai proses looping sebanyak {}'.format(loop_count))
    for i in range(loop_count):
        print(i)
    print("selesai")
    return time.sleep(5)


def looping_A():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    loop_count()
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return


def looping_B():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    loop_count()
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return


def looping_C():
    print (threading.currentThread().getName()+str('--> starting \n'))
    time.sleep(2)
    loop_count()
    print (threading.currentThread().getName()+str( '--> exiting \n'))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='looping #A', target=looping_A)
    t2 = threading.Thread(name='looping #B', target=looping_B)
    t3 = threading.Thread(name='looping #C',target=looping_C) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
