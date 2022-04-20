import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Mahasiswa(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def urut(self):

        with condition:

            if len(items) == 5:
                logging.info('no urut')
                condition.wait()

            items.pop()
            logging.info('no urut {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(7):
            time.sleep(2)
            self.urut()


class Dosen(threading.Thread):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def Quiz(self):

        with condition:

            if len(items) == 13:
                logging.info('Quiz {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('waktu Quiz {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.Quiz()


def main():
    urut = Mahasiswa(name='Mahasiswa')
    Quiz = Dosen(name='Dosen')

    urut.start()
    Quiz.start()

    urut.join()
    Quiz.join()


if __name__ == "__main__":
    main()