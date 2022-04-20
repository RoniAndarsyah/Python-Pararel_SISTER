import threading
import time

def daftar ():
    print (threading.currentThread().getName()+str('--> memulai daftar \n'))
    
    print (threading.currentThread().getName()+str( '--> daftar selesai \n'))
    time.sleep(2)
    return

def absen():
    print (threading.currentThread().getName()+str('--> mulai absen \n'))
    time.sleep(3)
    print (threading.currentThread().getName()+str( '--> selesai absen \n'))
    time.sleep(2)
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='daftar', target=daftar)
    t2 = threading.Thread(name='absen', target=absen)
    

    t1.start()
    t2.start()
  
    t1.join()
    t2.join()
   
