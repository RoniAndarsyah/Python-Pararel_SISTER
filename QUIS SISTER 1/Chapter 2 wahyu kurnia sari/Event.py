import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def jalan(e):
    logging.debug('Kamu lapar tidak')
    event_is_set = e.wait()
    logging.debug('Hari ini makan apa?: %s', event_is_set)


def pergi(e, t):
    while not e.isSet():
        logging.debug('Aku lapar sekali nih, makan sate yok')
        event_is_set = e.wait(t)
        logging.debug('Sate Apa: %s', event_is_set)
        if event_is_set:
            logging.debug('Sate Maranggi di warung Hj. Maya pasteur')
        else:
            logging.debug('Hayuk?')


if __name__ == "__main__":
    e = threading.Event()
    t1 = threading.Thread(name='wahyu',
                          target=jalan,
                          args=(e,))
    t1.start()

    t2 = threading.Thread(name='Kurnia',
                          target=pergi,
                          args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    logging.debug('Allhamdulillah kenyang')