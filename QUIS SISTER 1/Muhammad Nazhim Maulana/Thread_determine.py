import threading
import time
from random import randint

def First_Thread():
    if threading.activeCount() == 0:
        time.sleep(randint(5,10))
    print (threading.currentThread().getName()+str('--> mulai \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> selesai \n'))
    return

def Secon_Thread():
    if threading.activeCount() > 2:
        time.sleep(randint(5,10))
    print (threading.currentThread().getName()+str('--> mulai \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> selesai \n'))
    return

def Third_Thread():
    if threading.activeCount() > 3:
        time.sleep(randint(5,10))
    print (threading.currentThread().getName()+str('--> mulai \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> selesai \n'))
    return


if __name__ == "__main__":

    mulai = time.time()

    t1 = threading.Thread(name='thread pertama', target=First_Thread)
    t2 = threading.Thread(name='thread kedua', target=Secon_Thread)
    t3 = threading.Thread(name='thread ketiga',target=Third_Thread) 

    print("No. of active threads: " + str(threading.activeCount()))
    if threading.activeCount() > 0:
        time.sleep(randint(5,10))

    t1.start()

    print("No. of active threads: " + str(threading.activeCount()))
    t2.start()
    t3.start()
    print("No. of active threads: " + str(threading.activeCount()))

    t1.join()
    t2.join()
    t3.join()

    # End 
    print("Selesai")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - mulai))
