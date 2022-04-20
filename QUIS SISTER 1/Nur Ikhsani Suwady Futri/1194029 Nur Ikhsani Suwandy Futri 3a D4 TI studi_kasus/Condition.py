# Studi kasus tentang pembeliah Hp disuatu toko
import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Pembeli(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pembeli(self):

        with condition:

            if len(items) == 0:
                logging.info('tidak ada hp yang dibeli oleh pembeli')
                condition.wait()

            items.pop()
            logging.info('pembeli membeli 1 hp')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.pembeli()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def penjual(self):

        with condition:

            if len(items) == 10:
                logging.info('jumlah hp yang ditawarkan penjual sekarang {}. buah'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('penjual menawarkan hp dengan jumlah {} buah'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.penjual()


def main():
    producer = Penjual(name='Penjual')
    consumer = Pembeli(name='Pembeli')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
