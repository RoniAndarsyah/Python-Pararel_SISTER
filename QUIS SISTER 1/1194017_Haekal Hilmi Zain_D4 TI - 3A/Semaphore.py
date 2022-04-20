import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
table = 0
exist_table = [1, 4, 5, 7, 9, 10, 12, 15]


def reservation():
    logging.info('Melakukan reservasi meja makan')
    semaphore.acquire()


def resepsionis():
    global table
    time.sleep(1)
    logging.info('Memproses meja makan, silahkan menunggu')
    time.sleep(3)
    table = random.randint(1, 25)
    if table not in exist_table:
        exist_table.append(table)
        logging.info('meja No. {} kosong, proses dilanjutkan'.format(table))
        semaphore.release()
    else:
        logging.info('meja No. {} sudah terisi, pilih meja lainnya'.format(table))
        semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=reservation)
        t2 = threading.Thread(target=resepsionis)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
