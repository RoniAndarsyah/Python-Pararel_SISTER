
import threading
import time


def merah():
    print ('Lampu '+ str(threading.currentThread().getName())+( '--> Berhenti \n'))
    return

def kuning():
    print ('Lampu '+ str(threading.currentThread().getName())+( '--> Bersiap \n'))
    return

def hijau():
    time.sleep(2) #waktu jeda
    print ('Lampu '+str(threading.currentThread().getName())+( '--> Jalan \n'))
    return


t1 = threading.Thread(name='Merah', target=merah) 
t2 = threading.Thread(name='kuning', target=kuning) 
t3 = threading.Thread(name='hijau',target=hijau) 

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
