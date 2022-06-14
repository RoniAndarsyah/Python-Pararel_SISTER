#Dzul Jalali Wal Ikram

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def barengan(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("%s sampai dikelas pada tanggal %s" \
              %(name,datetime.fromtimestamp(now)))

def sendirian():
    name = multiprocessing.current_process().name
    now = time()
    print("%s sampai dikelas pada tanggal %s" \
          %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='Udin'\
            ,target=barengan,\
            args=(synchronizer,serializer)).start()
    Process(name='Asep'\
            ,target=barengan,\
            args=(synchronizer,serializer)).start()
    Process(name='Cecep'\
            ,target=sendirian).start()
    Process(name='Ucup'\
            ,target=sendirian).start()
    


