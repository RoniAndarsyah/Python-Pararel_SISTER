import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def pemenangundian():
    logging.info('pengundian tahunan bank dimulai semua nasabah harap menunggu')
    semaphore.acquire()
    logging.info('pemenang undian dengan nomor {} harap dapat datang ke bank'.format(item))


def nomorundian():
    global item
    time.sleep(3)
    item = random.randint(1, 10)
    logging.info('nomor {} adalah pemenang undian'.format(item))
    semaphore.release()


def main():
    for i in range(1):
        t1 = threading.Thread(target=pemenangundian)
        t2 = threading.Thread(target=nomorundian)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
