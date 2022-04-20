import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name
    print ("memulai proses pengocokan = %s \n" %name)
    time.sleep(3)
    print ("melakukan hasil akhir = %s \n" %name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
                        (name='ini proses saya',\
                         target=myFunc)

    #process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process\
                                (target=myFunc)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()
    
