import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Shopee(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def membeli(self):

        with condition:

            if len(items) == 0:
                logging.info('no items to checkout')
                condition.wait()

            items.pop()
            logging.info('chekout 1 item')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.membeli()


class Lazada(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def menjual(self):

        with condition:

            if len(items) == 10:
                logging.info('checkout {} items. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('chekout {} items '.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(1)
            self.menjual()


def main():
    shopee = Shopee(name='shopee')
    lazada = Lazada(name='lazada')

    shopee.start()
    lazada.start()

    shopee.join()
    lazada.join()


if __name__ == "__main__":
    main()
