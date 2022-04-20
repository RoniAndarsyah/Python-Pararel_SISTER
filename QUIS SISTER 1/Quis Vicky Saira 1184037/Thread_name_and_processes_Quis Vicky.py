from threading import Thread
import time
import os

class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Vicky nctzen {}".format(self.name)) #, " is {} \n".format(os.getpid()))

def main():
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")
    thread2 = MyThreadClass("Thread#2 ")
    thread3 = MyThreadClass("Thread#3 ")
  
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()


    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()

    # End 
    print("End")


if __name__ == "__main__":
    main()

    


