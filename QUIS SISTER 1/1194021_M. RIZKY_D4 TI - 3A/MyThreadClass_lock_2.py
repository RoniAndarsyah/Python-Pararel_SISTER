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

   def sum_pid_duration(self, pid):
      total = 0
      for i in range(self.duration):
         total += (i+1) * pid

      return total

   def run(self):
      #Acquire the Lock
      threadLock.acquire()      
      print("---> " + self.name + " berjalan, Proses ID adalah = " + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print("---> Total perhitungan Proses ID * Durasi = " + str(os.getpid()) + " * " + str(self.duration) + " = " + str(self.sum_pid_duration(os.getpid())))
      print("---> " + self.name + " Selesai\n")
      #Release the Lock


def main():
   start_time = time.time()

   # Thread Creation
   thread1 = MyThreadClass("Nomor Proses ID #1 ", randint(1,10))
   thread2 = MyThreadClass("Nomor Proses ID #2 ", randint(1,10))
   thread3 = MyThreadClass("Nomor Proses ID #3 ", randint(1,10))
   thread4 = MyThreadClass("Nomor Proses ID #4 ", randint(1,10))
   thread5 = MyThreadClass("Nomor Proses ID #5 ", randint(1,10))
   thread6 = MyThreadClass("Nomor Proses ID #6 ", randint(1,10))
   thread7 = MyThreadClass("Nomor Proses ID #7 ", randint(1,10))
   thread8 = MyThreadClass("Nomor Proses ID #8 ", randint(1,10))
   thread9 = MyThreadClass("Nomor Proses ID #9 ", randint(1,10))

   # Thread Running
   thread1.start()
   thread2.start()
   thread3.start()
   thread4.start()
   thread5.start()
   thread6.start()
   thread7.start()
   thread8.start()
   thread9.start()

   # Thread joining
   thread1.join()
   thread2.join()
   thread3.join()
   thread4.join()
   thread5.join()
   thread6.join()
   thread7.join()
   thread8.join()
   thread9.join()

   # End
   print("End")

   #Execution Time
   print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
   main()