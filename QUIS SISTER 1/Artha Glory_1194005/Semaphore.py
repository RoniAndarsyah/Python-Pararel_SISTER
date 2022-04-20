import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
nomor = (0,10)


def daftar_siswa():
    logging.info('memanggil siswa')
    semaphore.acquire()
    logging.info('daftar siswa: nomor absen {}'.format(nomor))


def kehadiran():
    global nomor
    time.sleep(1)
    nomor = random.randint(0, 10)
    logging.info('periksa kehadiran: nomor absen {}'.format(nomor))
    semaphore.release()


def main():
    for i in range(5):
        t1 = threading.Thread(target=daftar_siswa)
        t2 = threading.Thread(target=kehadiran)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()