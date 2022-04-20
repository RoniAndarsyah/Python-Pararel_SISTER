import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
room = 0
exist_room = [1, 4, 7, 2, 9, 13, 15, 20]


def reservation():
    logging.info('Melakukan reservasi hotel')
    semaphore.acquire()


def resepsionis():
    global room
    time.sleep(1)
    logging.info('Memproses hotel, silahkan menunggu')
    time.sleep(3)
    room = random.randint(1, 25)
    if room not in exist_room:
        exist_room.append(room)
        logging.info('Kamar No. {} kosong, proses dilanjutkan'.format(room))
        semaphore.release()
    else:
        logging.info('Kamar No. {} sudah terisi, pilih kamar lainnya'.format(room))
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
