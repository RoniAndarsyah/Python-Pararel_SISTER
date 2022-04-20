import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

semaphore = threading.Semaphore(0)
item = 0

def Penulis():
    logging.info('Permintaan dibuat')
    semaphore.acquire()
    logging.info('Penulis menulis surat nomor {}'.format(item))


def Pengirim():
    global item
    time.sleep(2)
    item = random.randint(0, 1000)
    logging.info('Pengirim merespon permintaan nomor {}'.format(item))
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=Penulis)
        t2 = threading.Thread(target=Pengirim)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
