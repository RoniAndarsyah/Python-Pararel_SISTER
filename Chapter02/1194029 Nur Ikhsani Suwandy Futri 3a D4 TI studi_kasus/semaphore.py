import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0) #menginisialisasi semphore ke 0 maka dapat 
#memperoleh event semphore agardapat mengsingkronkan dua atau lebih thread
item = 0 #sumber daya


def pemenangarisan(): #akam memperoleh data dari methode acquire jika perhitungannya 
    #0 dan akan memblokir methode acquire namun ketika perthitungan smaphorenya 
    # #lebih dari 0 maka nilai akan berkurang.
    logging.info('pengocokan arisan dimulai peserta harap menunggu')
    semaphore.acquire() # ketika nomorarisan melepas semaphore maka pemenanarisan 
    #akan memperoleh dan melakukan run pada bagian ini
    logging.info('pemenang arisan dengan nomor {} harap dapat datang ke tempat'.format(item))


def nomorarisan(): #akam membuat item dengan memanggil methode release
    global item
    time.sleep(3)
    item = random.randint(1, 10)
    logging.info('nomor {} adalah pemenang arisan'.format(item))
    semaphore.release()# dipanggil untuk membebaskan sumber daya 


def main():
    for i in range(1):
        t1 = threading.Thread(target=pemenangarisan)
        t2 = threading.Thread(target=nomorarisan)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
