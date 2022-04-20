from threading import Thread
import random
import time
import os

class subclassThread (Thread):
    def __init__(self, name):
      Thread.__init__(self)
      self.name = name
    def run(self): 
        threads = list()
        randomNumber = GenerateRandomNumber()
        print("hasil generate random number {} dari operasi {}".format(randomNumber, self.name))
def GenerateRandomNumber():
        listRandom = list()
        for i in range(0,10):
            listRandom.append(random.randint(10,100))
        return listRandom

def main(): 
    thread1 = subclassThread("Generate Random Number #1 \n")
    thread2 = subclassThread("Generate Random Number #2 \n")
  
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End")


if __name__ == "__main__":
    main()

    


