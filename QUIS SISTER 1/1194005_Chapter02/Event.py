import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
event = threading.Event()


class Tokped(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(1)
            event.wait()
            item = items.pop()
            logging.info('Tokped notify: {} dikelola oleh {}'\
                         .format(item, self.name))

class Blibli(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(1)
            item = random.randint(0, 10)
            items.append(item)
            logging.info('Blibli notify: item {} dikelola {}'\
                         .format(item, self.name))
            event.set()
            event.clear()

if __name__ == "__main__":
    t1 = Tokped()
    t2 = Blibli()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
