# Tugas Studi Kasus 
import logging
import threading
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

condition = threading.Condition()

class Mengantre():

    def pengunjung(self):
        logging.debug('pengunjung mulai mengantre...')
        
        with condition:
            logging.debug('pengunjung menunggu giliran...')
            condition.wait()
            logging.debug('sukses mendapat giliran')

    def loket(self):
        logging.debug('loket mulai dibuka...')
        
        with condition:
            logging.debug('loket memanggil nomor antrean...')
            na=0 
            na=random.randint(1,13)
            print('cek nomor antrean...')
            print('memanggil nomor antrean ke {}'.format(na))
            condition.notify()

antre = Mengantre()
pengunjung = threading.Thread(name='Pengunjung', target=antre.pengunjung)
loket = threading.Thread(name='loket', target=antre.loket)

pengunjung.start()
loket.start()

pengunjung.join()
loket.join()