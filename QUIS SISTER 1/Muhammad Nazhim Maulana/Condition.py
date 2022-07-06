import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()
print('\n ### Studi Kasus Sendiri ###')

class Pelanggan(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def beli(self):
        with condition:
            if len(items) > 5 and len(items) < 10:
                logging.info('Tidak ada yang bisa dibeli')
                condition.wait()

            items.pop()
            logging.info('Beli 1 roti')

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.beli()

class ProdusenRoti(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def membuat(self):

        with condition:

            if len(items) == 15:
                logging.info('roti diproduksi {}. Berhenti'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total roti {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.membuat()


def main():
    produsen = ProdusenRoti(name='Produsen Roti')
    konsumen = Pelanggan(name='Konsumen')

    produsen.start()
    konsumen.start()

    produsen.join()
    konsumen.join()


if __name__ == "__main__":
    main()