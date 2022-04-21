import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()

# yg ga boleh diganti def __init__
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('no items to tepung')
                condition.wait()

            items.pop()
            logging.info('tepung 1 ')

            condition.notify()

    def run(self):
        for i in range(3):
            time.sleep(2)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 3:
                logging.info('jenis tepung {}. selesai'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total  {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(3):
            time.sleep(0.2)
            self.produce()


def main():
    producer = Producer(name='tepung')
    consumer = Consumer(name='kue')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
