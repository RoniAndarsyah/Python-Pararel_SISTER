import multiprocessing
import time
from time import ctime

def foo():
    name = multiprocessing.current_process().name
    print ("Produk %s pada tanggal %s \n" %(name, ctime()))
    if name == 'retur':
        for i in range(0,5):
            print('SKU produk %d \n' %i)
        time.sleep(1)
    else:
        for i in range(5,10):
            print('SKU produk %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='retur berhasil',\
                          target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='retur berhasil',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

