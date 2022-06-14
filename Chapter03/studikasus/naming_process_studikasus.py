import multiprocessing
import time
import random

def approveRole():
    name = multiprocessing.current_process().name
    userId = random.randrange(0, 20)
    print ("Admin mulai melakukan = %s \n" %name)
    time.sleep(3)
    print ("Admin selesai mengapprove Role Request user dengan ID %s sebagai Owner  \n" %userId)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process\
                        (name='Approve Role User',\
                         target=approveRole)

    process_with_default_name = multiprocessing.Process\
                                (target=approveRole)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()