import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def kendaraan(e):
    logging.debug('sebentar')
    event_is_set = e.wait()
    logging.debug('roda berapa?: %s', event_is_set)

def pergi(e, t):
    while not e.isSet():
        logging.debug('warna apa kendaraannya?')
        event_is_set = e.wait(t)
        logging.debug('warna merah: %s', event_is_set)
        if event_is_set:
            logging.debug('terimakasih informasinya')
        else:
            logging.debug('mobilnya bagus juga?')

if _name_ == "_main_":
    e = threading.Event()
    t1 = threading.Thread(name='wahyu', 
                      target=kendaraan,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='fay', 
                      target=pergi, 
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('keren juga ya')