import threading
import time


def kelas_sistem_tersebar():
    print (threading.currentThread().getName()+str('--> mulai kelas jam 7.50 \n'))
    time.sleep(4)
    print (threading.currentThread().getName()+str( '--> selesai kelas jam 12.00 \n'))
    time.sleep(2)
    return

def kelas_bahasa_inggris():
    print (threading.currentThread().getName()+str('--> mulai kelas jam 13.00 \n'))
    time.sleep(4)
    print (threading.currentThread().getName()+str( '--> selesai kelas jam 17.10 \n'))
    time.sleep(2)
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='kelas_sistem_tersebar', target=kelas_sistem_tersebar)
    t2 = threading.Thread(name='kelas_bahasa_inggris', target=kelas_bahasa_inggris)
  

    t1.start()
    t2.start()

    t1.join()
    t2.join()
 
