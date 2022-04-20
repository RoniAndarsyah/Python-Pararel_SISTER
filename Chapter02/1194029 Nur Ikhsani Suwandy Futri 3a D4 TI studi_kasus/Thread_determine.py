# studi kasus cerdas cermat
import threading
import time

def peserta1():
    print (threading.currentThread().getName()+str('--> memulai mengerjakan \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> berhenti mengerjakan \n'))
    return

def peserta2():
    print (threading.currentThread().getName()+str('--> memulai mengerjakan \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> berhenti mengerjakan \n'))
    return

def peserta3():
    print (threading.currentThread().getName()+str('--> memulai mengerjakan \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> berhenti mengerjakan \n'))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='peserta dengan nomor urut 1', target=peserta1)
    t2 = threading.Thread(name='peserta dengan nomor urut 2', target=peserta2)
    t3 = threading.Thread(name='peserta dengan nomor urut 3',target=peserta3) 

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
