import threading
import time

from django.urls import clear_script_prefix

def Minum_Sahur():
    print (threading.currentThread().getName()+str('--> Energen Coklat \n'))
    time.sleep(3)
    print (threading.currentThread().getName()+str( '-->selesai minum energen coklat \n'))
    return

def Minum_Buka():
    print (threading.currentThread().getName()+str('--> Es Buah \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> selesai minum es buah \n'))
    return




if __name__ == "__main__":

    t1 = threading.Thread(name='Minum_Sahur', target=Minum_Sahur)
    t2 = threading.Thread(name='Minum_Buka', target=Minum_Buka)
   

    t1.start()
    t2.start()
    clear_script_prefix

    t1.join()
    t2.join()
  
