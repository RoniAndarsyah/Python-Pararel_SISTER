import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def pelanggan():
    logging.info('Pelanggan meminta antrian')
    semaphore.acquire()
    logging.info('Pelanggan menerima: antrian no {}'.format(item))


def antrian():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('antrian generate: no antrian {}'.format(item))
    semaphore.release()


def main():
    for i in range(3):
        t1 = threading.Thread(target=pelanggan)
        t2 = threading.Thread(target=antrian)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
