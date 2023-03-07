import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def jalan(e):
    logging.debug('sebentar')
    event_is_set = e.wait()
    logging.debug('kamu ada dimana?: %s', event_is_set)

def pergi(e, t):
    while not e.isSet():
        logging.debug('ayo kita pergi, kemana yaa?')
        event_is_set = e.wait(t)
        logging.debug('ke bandung yok: %s', event_is_set)
        if event_is_set:
            logging.debug('terimakasih waktunya')
        else:
            logging.debug('mobilnya bagus juga?')

if __name__ == "__main__":
    e = threading.Event()
    t1 = threading.Thread(name='bintang', 
                      target=jalan,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='bulan', 
                      target=pergi, 
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('melelahkan juga ya')