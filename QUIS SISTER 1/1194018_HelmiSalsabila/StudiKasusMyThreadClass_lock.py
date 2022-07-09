import threading
import time
import os
from threading import Thread
from random import randint

# Threading melakukan konkurensi untuk mengeksekusi sebuah operasi
# Threading memisahkan sebgian kode dan mengeksekusi di proses yg dibuatnya sendiri
# tentukan limit prosesnya agar tidak menghabiskan ruang cpu dan ram
# Menggunakan fungsi lock yang akan membungkus beberapa perintah dalam method untuk di jalnkankan dulu baru apabila kelar akan menjalankan printah selanjutnya setelah syntax lock release

# Lock Definition
threadLock = threading.Lock()

class MyThreadClass (Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration
    def run(self):
        #Acquire the Lock
        #getpid untuk mendapatkan ID proses dari proses saat ini
        threadLock.acquire()      
        print ("---> " + self.name + \
                "running, ID "\
                + str(os.getpid()) + "\n")
        time.sleep(self.duration)
        print("Waktu ", self.duration, "seconds")
        print ("---> " + self.name + " selesai\n")
    #Release the Lock
        threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Proses Thread 1 ", randint(1,10))
    thread2 = MyThreadClass("Proses Thread 2 ", randint(1,10))
    thread3 = MyThreadClass("Proses Thread 3 ", randint(1,10))
    thread4 = MyThreadClass("Proses Thread 4 ", randint(1,10))
    thread5 = MyThreadClass("Proses Thread 5 ", randint(1,10))


    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Thread joining (proses pengembalian elemen dari proses yg sudah selesai)
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    

