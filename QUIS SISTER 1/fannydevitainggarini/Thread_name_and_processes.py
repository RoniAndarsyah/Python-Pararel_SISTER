from threading import Thread
import time
import os

class MyThreadClass (Thread):
   def _init_(self, name):
      Thread._init_(self)
      self.name = name
 
   def run(self):
       print("jangan menyerah menggapai mimpi {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Thread Running
    thread1.start()
    thread2.start()


    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("tetap semangat!!")


if _name_ == "_main_":
    main()