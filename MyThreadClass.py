import time
import os
from random import randint
from threading import Thread

class MyThreadClass (Thread):
   def __init__(self, name, duration):
      Thread.__init__(self)
      self.name = name
      self.duration = duration
   def run(self):
      print ("---> " + self.name + \
             " running, belonging to process ID "\
             + str(os.getpid()) + "\n")
      time.sleep(self.duration)
      print ("---> " + self.name + " over\n")


def main():
    start_time = time.time()
    
    # Thread Creation
    Audry1 = MyThreadClass("Audry ", randint(1,5))
    Artha2 = MyThreadClass("Artha ", randint(1,5))
    Lina3 = MyThreadClass("Lina ", randint(1,5))
    Jimin4 = MyThreadClass("Jimin ", randint(1,5))
    Wooyoung5 = MyThreadClass("Wooyoung ", randint(1,5))
    Haruto6 = MyThreadClass("Haruto ", randint(1,5))

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
    print("Ujian Selesai")

    #Execution Time
    print("--- %s detik ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    


