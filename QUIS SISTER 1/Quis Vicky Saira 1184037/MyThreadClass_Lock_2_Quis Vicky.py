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
             " Games nya idol "\
             + str(os.getpid()) + "\n")
      threadLock.release()
      time.sleep(self.duration)
      print ("---> " + self.name + " over\n")
      #Release the Lock


def main():
    start_time = time.time()
    
    # Thread Creation
    vicky1 = MyThreadClass("Vicky#1 ", randint(1,10))
    heeseung2 = MyThreadClass("Heeseung#2 ", randint(1,10))
    jake3 = MyThreadClass("Jake#3 ", randint(1,10))
    haruto4 = MyThreadClass("Haruto#4 ", randint(1,10))
    winwin5 = MyThreadClass("Winwin#5 ", randint(1,10))
    hyunsuk6 = MyThreadClass("Hyunsuk#6 ", randint(1,10))
    junkyu7 = MyThreadClass("Junkyu#7 ", randint(1,10))
    jisung8 = MyThreadClass("Jisung#8 ", randint(1,10))
    minho9 = MyThreadClass("Minho#9 ", randint(1,10))

    # Thread Running
    vicky1.start()
    heeseung2.start()
    jake3.start()
    haruto4.start()
    winwin5.start()
    hyunsuk6.start()
    junkyu7.start()
    jisung8.start()
    minho9.start()

    # Thread joining
    vicky1.join()
    heeseung2.join()
    jake3.join()
    haruto4.join()
    winwin5.join()
    hyunsuk6.join()
    junkyu7.join()
    jisung8.join()
    minho9.join()

    # End
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

    


