import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Outbound(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pick(self):
        with condition:
            if len(items) == 0:
                logging.info('Barang kosong. Tidak ada barang yang di ambil')
                condition.wait()

            items.pop()
            logging.info('Mengambil 1 barang')
            logging.info('Sisa barang dalam gudang {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(21):
            time.sleep(2)
            self.pick()


class Inbound(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def store(self):
        with condition:
            if len(items) == 10:
                logging.info('Total barang dalam gudang {}. Gudang penuh'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('Memasukan barang pada gudang {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.store()


def main():
    inbound = Inbound(name='Inbound')
    outbound = Outbound(name='Outbound')

    inbound.start()
    outbound.start()

    inbound.join()
    outbound.join()


if __name__ == "__main__":
    main()
