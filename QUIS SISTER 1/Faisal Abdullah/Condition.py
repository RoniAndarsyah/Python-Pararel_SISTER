import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition() 



class Kosumen(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pakai(self):

        with condition: 

            if len(items) == 0:
                logging.info('Tidak ada barang yang dapat dibeli')
                condition.wait()

            items.pop() 
            logging.info('Kamu membeli 1 barang')

            condition.notify() 
                               

    def run(self):
        for i in range(20):
            time.sleep(2) 
            self.pakai()


class Pabrik(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def jual(self):

        with condition: 

            if len(items) == 10:
                logging.info('Di etalase terdapat {} item. Tidak cukup tempat. Produksi berhenti sementara'.format(len(items)))
                condition.wait() 

            items.append(1) 
            logging.info('Terdapat {} barang saat ini'.format(len(items))) 

            condition.notify() 
                                

    def run(self):
        for i in range(20):
            time.sleep(0.5) 
            self.jual()


def main():
    kosumen = Pabrik(name='Pabrik') 
    pabrik = Kosumen(name='Kosumen') 

    pabrik.start()
    kosumen.start()

    pabrik.join()
    kosumen.join()


if __name__ == "__main__":
    main()
