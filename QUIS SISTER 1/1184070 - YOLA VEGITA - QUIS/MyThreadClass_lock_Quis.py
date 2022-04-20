#!/usr/bin/python

import os
import threading
import time
from threading import Thread
from random import randint

exitFlag = 0
lock = threading.Lock()
bounded_semaphore = threading.BoundedSemaphore(100) #penggunaan semaphore

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print ("Exiting " + self.name)

#membuat fungsi
def f1():
    bounded_semaphore.acquire()
    print("%s acquired lock." % (threading.current_thread().name))
    print(bounded_semaphore._value)
    bounded_semaphore.release()
    print("%s released lock." % (threading.current_thread().name))
    print(bounded_semaphore._value)
   

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f1)
t3 = threading.Thread(target=f1)
t4 = threading.Thread(target=f1)
t5 = threading.Thread(target=f1)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("Main Thread Exited.", threading.main_thread())

print ("Exiting Main Thread")
