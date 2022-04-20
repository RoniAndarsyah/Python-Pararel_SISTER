import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def jalan(e):
    logging.debug('Tunggu dulu')
    event_is_set = e.wait()
    logging.debug('kamu ada dimana?: %s', event_is_set)

def pergi(e, t):
    while not e.isSet():
        logging.debug('Kita healing kuy, kemana yaa serunya?')
        event_is_set = e.wait(t)
        logging.debug('ke Jogja kuy: %s', event_is_set)
        if event_is_set:
            logging.debug('terimakasih waktunya')
        else:
            logging.debug('Naik becak?')

if __name__ == "__main__":
    e = threading.Event()
    t1 = threading.Thread(name='Vicky', 
                      target=jalan,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='Safira', 
                      target=pergi, 
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Capek juga')