# Tugas Studi Kasus

import threading
import time
import os
from threading import Thread
from random import randint
 
# Lock Definition
threadLock = threading.Lock()

class MyThread(Thread):
  # overriding constructor
  def __init__(self, i, duration):
    # calling parent class constructor
    Thread.__init__(self)
    self.x = i
    self.duration = duration 

  # define your own run method
  def run(self):
   # Acquire the Lock
   threadLock.acquire() 

   print("Value stored is: ", self.x)

   # Release the Lock
   threadLock.release()
   time.sleep(self.duration)
   print("Exiting thread with value: ", self.x)


thread1 = MyThread(1, randint(1,10))
thread2 = MyThread(2, randint(1,10))
thread3 = MyThread(3, randint(1,10))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

