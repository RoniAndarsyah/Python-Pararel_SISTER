import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
antrean = 0


def pelanggan():
    logging.info('Pelanggan sedang antre')
    semaphore.acquire()
    logging.info('Pelanggan di panggil: antrean ke {}'.format(antrean))


def dokterHewan():
    global antrean
    time.sleep(3)
    antrean = random.randint(0, 1000)
    logging.info('Dokter memanggil: antrean ke {}'.format(antrean))
    semaphore.release()
    logging.info('Berpindah')


def main():
    for i in range(1):
        t1 = threading.Thread(target=pelanggan)
        t2 = threading.Thread(target=dokterHewan)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()