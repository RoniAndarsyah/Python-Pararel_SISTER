# Tugas Studi Kasus

import threading
import time
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class MyThread(Thread):
  def __init__(self, i, duration):
    Thread.__init__(self)
    self.x = i
    self.duration = duration 

  def run(self):
   # Acquire the Lock
   threadLock.acquire() 

   print("Value stored is: ", self.x)
   time.sleep(self.duration)
   print("Exiting thread with value: ", self.x)

   # Release the Lock
   threadLock.release()
    

thread1 = MyThread(1, randint(1,10))
thread2 = MyThread(2, randint(1,10))
thread3 = MyThread(3, randint(1,10))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
