# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:28:19 2022

@author: Acer
"""

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
                    
def jalan(e):
    logging.debug('sepertinya kita harus pergi')
    event_is_set = e.wait()
    logging.debug('kamu ada dimana?: %s', event_is_set)

def pergi(e, t):
    while not e.isSet():
        logging.debug('ayo kita pergi, kemana yaa?')
        event_is_set = e.wait(t)
        logging.debug('kita pergi ke jakarta aja : %s', event_is_set)
        if event_is_set:
            logging.debug('ayok')
        else:
            logging.debug('mobilnya bagus juga ya')

if __name__ == "__main__":
    e = threading.Event()
    t1 = threading.Thread(name='Caca', 
                      target=jalan,
                      args=(e,))
    t1.start()

    t2 = threading.Thread(name='Cici', 
                      target=pergi, 
                      args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('melelahkan juga ya')