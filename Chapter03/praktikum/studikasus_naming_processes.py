import multiprocessing
import time
from time import ctime

def myFunc():
    name = multiprocessing.current_process().name
    print ("Starting process name = %s \n pada tanggal %s\n" % (name, ctime()))
    time.sleep(3)
    print ("Exiting process name = %s \n pada tanggal %s\n" % (name, ctime()))

if __name__ == '__main__':
    process_with_name1 = multiprocessing.Process\
                        (name='Penamaan produk',\
                        target=myFunc)
    process_with_name2 = multiprocessing.Process\
                        (name='Penomoran produk',\
                        target=myFunc)

    #process_with_name.daemon = True

    process_with_default_name1 = multiprocessing.Process\
                                (target=myFunc)
    process_with_default_name2 = multiprocessing.Process\
                                (target=myFunc)

    process_with_name1.start()
    process_with_name2.start()
    process_with_default_name1.start()
    process_with_default_name2.start()

    process_with_name1.join()
    process_with_name2.join()
    process_with_default_name1.join()
    process_with_default_name2.join()
    
    print('Selesai proses')

    
