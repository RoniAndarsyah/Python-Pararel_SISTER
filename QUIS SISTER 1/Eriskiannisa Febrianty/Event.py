# Tugas Studi Kasus
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def wait_for_event(e):
    logging.debug('Menunggu film dimulai...')
    event_is_set = e.wait()
    logging.debug('Film dimulai: %s', event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('Menunggu Film Selesai')
        event_is_set = e.wait(t)
        logging.debug('Film dimulai: %s', event_is_set)
        if event_is_set:
            logging.debug('Memproses Film')
        else:
            logging.debug('Iklan')

if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='blocking', target=wait_for_event,args=(e,))
    t2 = threading.Thread(name='non-blocking', target=wait_for_event_timeout, args=(e, 2))
    t1.start()
    t2.start()

    logging.debug('Menunggu sebelum film dimulai')
    time.sleep(3)
    e.set()
    logging.debug('Film dimulai')