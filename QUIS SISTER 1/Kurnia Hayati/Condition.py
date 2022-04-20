import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Pasien(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def daftar(self):

        with condition:

            if len(items) == 5:
                logging.info('no antri')
                condition.wait()

            items.pop()
            logging.info('no antri {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(5):
            time.sleep(2)
            self.antri()


class Dokter(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def pendaftaran(self):

        with condition:

            if len(items) == 13:
                logging.info('pendaftaran {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('waktu pendaftaran {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.7)
            self.pendaftaran()


def main():
    antri = mahasiswa(name='mahasiswa')
    pendaftaran = krs(name='krs')

    antri.start()
    pendaftaran.start()

    antri.join()
    pendaftaran.join()


if _name_ == "_main_":
    main()