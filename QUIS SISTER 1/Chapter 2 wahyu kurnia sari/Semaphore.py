# importing the modules
from threading import *
import time

# creating thread instance where count = 3
obj = Semaphore(1)


# creating instance
def display(name):
    # calling acquire method
    obj.acquire()
    for i in range(1):
        print('Jenis Sate, ', end='')
        time.sleep(1)
        print(name)

        # calling release method
        obj.release()


# creating multiple thread
t1 = Thread(target=display, args=('Taichan-1',))
t2 = Thread(target=display, args=('Maranggi-2',))
t3 = Thread(target=display, args=('Kambing-3',))
t4 = Thread(target=display, args=('Ayam-4',))
t5 = Thread(target=display, args=('Lilit-5',))

# calling the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()