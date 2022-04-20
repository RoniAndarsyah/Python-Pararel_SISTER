import time
import os
from random import randint
from threading import Thread

class MyThreadClass (Thread):
   def _init_(self, name, duration):
      Thread._init_(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " mulai kuis, NPM "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " melakukan kuis\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    wahyu1 = MyThreadClass("wahyu ", randint(6,10))
    ayna2 = MyThreadClass("ayna ", randint(6,10))
    farhan3 = MyThreadClass("farhan ", randint(6,10))
    sinta4 = MyThreadClass("Jimin ", randint(6,10))
    via5 = MyThreadClass("sinta ", randint(6,10))
    ririn6 = MyThreadClass("ririn ", randint(6,10))
  
    # Thread Running
    wahyu1.start()
    ayna2.start()
    farhan3.start()
    sinta4.start()
    via5.start()
    ririn6.start()

    # Thread joining
    wahyu1.join()
    ayna2.join()
    farhan3.join()
    sinta4.join()
    via5.join()
    ririn6.join()

    # End 
    print("End")

    #Execution Time
    print("--- waktu pengerjaan kuis %s seconds ---" % (time.time() - start_time))


if _name_ == "_main_":
    main()