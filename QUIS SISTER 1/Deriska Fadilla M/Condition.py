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

            if len(items) > 6 and len(items) < 9:
                logging.info('tidak ada yang bisa di beli')
                condition.wait()

            items.pop()
            logging.info('beli 1 mangga')

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.beli()


class Penjualsedang(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def membuat(self):

        with condition:

            if len(items) == 10:
                logging.info('mangga diproses {}. berhenti'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total mangga {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(15):
            time.sleep(0.5)
            self.membuat()


def main():
    penjualsedang = Penjualsedang(name='penjualsedang')
    pembeli = Pembeli(name='pembeli')

    penjualsedang.start()
    pembeli.start()

    penjualsedang.join()
    pembeli.join()


if __name__ == "__main__":
    main()
