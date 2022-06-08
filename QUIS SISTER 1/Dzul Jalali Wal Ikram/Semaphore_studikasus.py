import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def nasabah():
    logging.info('Nasabah Menunggu nomor Antriannya dipanggil')
    semaphore.acquire()
    logging.info('Nasabah dengan nomor antrian %d menuju Customer Service' % (item))


def cs():
    global item
    time.sleep(3)
    item = random.randint(0, 100)
    logging.info('Customer Service memanggil nomor antrian {}'.format(item))
    semaphore.release()


def main():
    for i in range(5):
        t1 = threading.Thread(target=nasabah)
        t2 = threading.Thread(target=cs)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
