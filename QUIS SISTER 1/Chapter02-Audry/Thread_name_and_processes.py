from threading import Thread
import time
import os

class hewan (Thread): 
   def __init__(self, name): 
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       print("Jenis-jenis hewan: {}".format(self.name)) 

def main():
    from random import randint
    thread1 = hewan("Amfibi ") 
    thread2 = hewan("Mamalia")
    thread3 = hewan("Aves")
    thread4 = hewan("Reptil")
    thread5 = hewan("Serangga")
  
    # memulai thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Thread joining and finish to join
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    #End 
    print("Sekian")


if __name__ == "__main__":
    main()

    


