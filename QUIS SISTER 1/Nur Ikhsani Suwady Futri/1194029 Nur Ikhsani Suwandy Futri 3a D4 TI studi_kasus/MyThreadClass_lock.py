#studi kasus tentang perlombaan cerdas cermat mengenai ruangan dan soal
import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyThreadClass (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " kodenya adalah "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " selesai diberikan kodenya\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    thread1 = MyThreadClass("Ruangan Fisika yang digunakan ", randint(1,10))
    thread2 = MyThreadClass("Soal 1", randint(1,10))

   

    # Thread Running
    thread1.start()
    thread2.start()

    

    # Thread joining
    thread1.join()
    thread2.join()

    

    # End 
    print("Selamat Datang di Ruangan Fisika para peserta acara lomba cerdas cermat ")
    print("Selamat Mengerjakan soal")

    #Execution Time
    print("waktu yang dibutuhkan untuk mengerjakan soal %s  seconds soal" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    


