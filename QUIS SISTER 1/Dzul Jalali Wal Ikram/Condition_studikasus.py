import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Siswa(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def siswa(self):

        with condition:

            if len(items) == 0:
                logging.info('tidak ada makanan untuk dikonsumsi')
                condition.wait()

            items.pop()
            logging.info('mengkonsumsi 1 makanan')

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.siswa()


class Kantin(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def kantin(self):

        with condition:

            if len(items) == 10:
                logging.info('makanan disediakan {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('jumlah makanan yang disediakan {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.5)
            self.kantin()


def main():
    kantin = Kantin(name='Kantin')
    siswa = Siswa(name='Siswa')

    kantin.start()
    siswa.start()

    kantin.join()
    siswa.join()


if __name__ == "__main__":
    main()
