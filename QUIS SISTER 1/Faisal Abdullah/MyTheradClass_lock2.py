import threading
import time

konci2 = threading.Lock()
#lock = digunakan untuk block sebuah thread untuk melakukan execute sebelum thread lain beres
#lock2 = posisi dari method release() yang diubah akan mempengaruhi output

def orang_pertama(konci2):
    konci2.acquire()
    print('orang - 1 sedang menggunakan kamar mandi')
    time.sleep(1)
    print('orang - 1 sudah selesai')
    # konci2.release()

def orang_kedua(konci2):
    # konci2.acquire()
    print('orang - 2 sedang menggunakan kamar mandi')
    konci2.release()
    time.sleep(1)
    print('orang - 2 sudah selesai')
   

t1 = threading.Thread(target=orang_pertama, args=(konci2, ))
t2 = threading.Thread(target=orang_kedua, args=(konci2, ))

t1.start()
t2.start()

t1.join()
t2.join()
