import logging
import threading
import time
import random
import names # Didapatkan dengan pip install names

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

people = []
event = threading.Event()


class Gamer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(random.randint(0, 5))
            event.wait()
            orang = people.pop()
            logging.info('Gamer megabari orang bernama: {} sudah selesai oleh {}'\
                         .format(orang, self.name))

class ComputerSeller(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(random.randint(0, 19)):
            time.sleep(random.randint(0, 5))
            orang = names.get_full_name()
            people.append(orang)
            logging.info('Computer Seller mengabari: orang bernama {} oleh {}'\
                         .format(orang, self.name))
            event.set()
            event.clear()

if __name__ == "__main__":
    pertama = ComputerSeller()
    kedua = Gamer()

    pertama.start()
    kedua.start()

    pertama.join()
    kedua.join()
