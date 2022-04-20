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

    def beli(self):

        with condition:

            if len(items) == 0:
                logging.info('Tidak ada makanan yang dapat dibeli')
                condition.wait()

            items.pop()
            logging.info('Kamu membeli 1 item makanan')

            condition.notify() 

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.beli()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def jual(self):

        with condition:

            if len(items) == 10:
                logging.info('Di etalase terdapat {} item. Tidak cukup tempat. Produksi berhenti sementara'.format(len(items)))
                condition.wait() 

            items.append(1)
            logging.info('Terdapat {} item makanan saat ini'.format(len(items)))

            condition.notify() 

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.jual()


def main():
    pembeli = Penjual(name='Penjual')
    penjual = Pembeli(name='Pembeli')

    penjual.start()
    pembeli.start()

    penjual.join()
    pembeli.join()


if __name__ == "__main__":
    main()
