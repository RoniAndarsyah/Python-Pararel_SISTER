import logging
import multiprocessing
import threading
from time import sleep
from random import randrange

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

foods = []
condition = threading.Condition()
num_chef = 3
chef = ['Chef 1', 'Chef 2', 'Chef 3']
synchronizerThreading = threading.Barrier(num_chef)
synchronizerMultiProc = multiprocessing.Barrier(num_chef)

class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs = kwargs['kwargs']

    def consume(self):
        with condition:
            if len(foods) == 0:
                logging.info('Tidak ada makanan yang di makan, status : {}'.format(self.kwargs["stat3"]))
                condition.wait()
            foods.pop()
            logging.info('Memakan 1 makanan, status : {}'.format(self.kwargs["stat1"]))
            condition.notify()

    def run(self):
        for i in range(21):
            sleep(2)
            self.consume()

class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs = kwargs['kwargs']

    def produce(self):
        with condition:
            if len(foods) == 10:
                logging.info('Total makakanan dibuat {}. Berhenti, status : {}'.format(len(foods), self.kwargs['stat2']))
                condition.wait()
            foods.append(1)
            logging.info('Total makanan {}'.format(len(foods)))
            condition.notify()

    def run(self):
        for i in range(20):
            sleep(0.5)
            self.produce()

def chef_challengeThread():
    name = chef.pop()
    sleep(randrange(2, 5))
    print('%s menyelesaikan lomba Thread ' % (name))
    synchronizerThreading.wait()


def chef_challengeMultiProc(synchronizerMultiProc, serializer):
    name = multiprocessing.current_process().name
    sleep(randrange(2, 5))
    synchronizerMultiProc.wait()
    with serializer:
        print('%s menyelesaikan lomba Multi Proc ' % (name))

def main():
    print('Lomba Masak Multi Proc Mulai')
    for i in range(num_chef):
        serializer = multiprocessing.Lock()
        multiprocessing.Process(name=chef[i], target=chef_challengeMultiProc, args=(synchronizerMultiProc,serializer)).start()

    threads = []
    print('Lomba Masak Thread Mulai')
    for i in range(num_chef):
        threads.append(threading.Thread(target=chef_challengeThread))
        threads[-1].start()
    for thread in threads:
        thread.join()

    producer = Producer(name='Producer', kwargs={"stat1": 'Berhasil', "stat2": "Kepenuhan", "stat3": "Kosong"})
    consumer = Consumer(name='Consumer', kwargs={"stat1": 'Berhasil', "stat2": "Kepenuhan", "stat3": "Kosong"})

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
