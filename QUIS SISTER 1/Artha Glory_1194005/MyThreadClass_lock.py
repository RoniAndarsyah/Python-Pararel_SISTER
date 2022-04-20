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
             " Mulai Ujian, Nomor Ujian "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " Selamat mengerjakan\n")
      #Release the Lock
      threadLock.release()


def main():
    start_time = time.time()
    # Thread Creation
    Audry1 = MyThreadClass("Audry ", randint(6,10))
    Artha2 = MyThreadClass("Artha ", randint(6,10))
    Lina3 = MyThreadClass("Lina ", randint(6,10))
    Jimin4 = MyThreadClass("Jimin ", randint(6,10))
    Wooyoung5 = MyThreadClass("Wooyoung ", randint(6,10))
    Haruto6 = MyThreadClass("Haruto ", randint(6,10))

    # Thread Running
    Audry1.start()
    Artha2.start()
    Lina3.start()
    Jimin4.start()
    Wooyoung5.start()
    Haruto6.start()

    # Thread joining
    Audry1.join()
    Artha2.join()
    Lina3.join()
    Jimin4.join()
    Wooyoung5.join()
    Haruto6.join()


    # End 
    print("Selesai Ujian")

    #Execution Time
    print("--- waktu ujian %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    


