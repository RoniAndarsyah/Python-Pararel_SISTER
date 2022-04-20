from threading import Thread
import time
import os

class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("jangan menunggu yang tidak pasti {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
  
    # Thread Running
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # End 
    print("lebih baik rebahan dari pada menunggu")


if __name__ == "__main__":
    main()