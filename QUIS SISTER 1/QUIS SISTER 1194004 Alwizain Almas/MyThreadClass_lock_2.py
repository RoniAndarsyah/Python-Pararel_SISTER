import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class PitStopF1 (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print ("---> " + self.name + \
             " mulai mengganti roda F1, ini merupakan roda pengganti F1 ke "\
             + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> " + self.name + " selesai mengganti roda F1\n")
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    thread1 = PitStopF1("Montir 1 ", randint(1,5))
    thread2 = PitStopF1("Montir 2 ", randint(1,5))
    thread3 = PitStopF1("Montir 3 ", randint(1,5))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()

    # End
    print("Mobil F1 melaju kembali ke jalur balapan")

    #Execution Time
    print("Service pitstop memakan waktu %s detik" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    


