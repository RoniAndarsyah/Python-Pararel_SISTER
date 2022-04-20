# Tugas Studi Kasus 
import time
import os
from random import randint
from threading import Thread

class MyThread(Thread):
  def __init__(self, i, duration):
    Thread.__init__(self)
    self.x = i
    self.duration = duration 

  def run(self):
    print("Value stored is: ", self.x)
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

