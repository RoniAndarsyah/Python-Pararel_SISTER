from threading import Thread
import time
import os

class takjil (Thread): #thread itu modul didalam treading
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("buka puasa enaknya makan {}".format(self.name)) 

def main():
    from random import randint
    # Delcare object of takjil class
    thread1 = takjil("es buah ")
    thread2 = takjil("es kelapa ")
    thread3 = takjil("nasi padang")
  
    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()


    # Thread joining and finish to join
    thread1.join()
    thread2.join()
    thread3.join()

    # End 
    print("Selamat berpuasa")


if __name__ == "__main__":
    main()

    


