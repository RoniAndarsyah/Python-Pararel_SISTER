import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

def worker(i,dt,e):
    tStart=time.time()
    e.wait(dt)
    logging.debug('{0} tried to wait {1} seconds but really waited {2}'.format(i,dt, time.time()-tStart ))


e = threading.Event()

maxThreads=10
for i in range(maxThreads):
    dt=1+i # (s)
    w = threading.Thread(target=worker, args=(i,dt,e))
    w.start()