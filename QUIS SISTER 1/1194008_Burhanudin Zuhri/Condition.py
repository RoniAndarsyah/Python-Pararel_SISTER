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

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('Tidak ada sepeda yang dapat dibeli')
                condition.wait()

            items.pop()
            logging.info('Anda membeli 1 buah sepeda')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 10:
                logging.info('Pada toko terdapat {} buah sepeda. Produksi berhenti untuk sementara'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('Terdapat {} buah sepeda saat ini'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()


def main():
    penjual = Penjual(name='Penjual')
    pembeli = Pembeli(name='Pembeli')

    penjual.start()
    pembeli.start()

    penjual.join()
    pembeli.join()


if __name__ == "__main__":
    main()
