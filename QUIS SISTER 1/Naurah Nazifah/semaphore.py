import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def pemenangarisan():
    logging.info('pengocokan arisan dimulai peserta harap menunggu')
    semaphore.acquire()
    logging.info('pemenang arisan dengan nomor {} harap dapat datang ke tempat'.format(item))


def nomorarisan():
    global item
    time.sleep(3)
    item = random.randint(1, 10)
    logging.info('nomor {} adalah pemenang arisan'.format(item))
    semaphore.release()


def main():
    for i in range(5):
        t1 = threading.Thread(target=pemenangarisan)
        t2 = threading.Thread(target=nomorarisan)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
