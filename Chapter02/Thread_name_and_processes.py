from threading import Thread
import time
import os
from random import randint

class MyThreadClass (Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("ID of process running {}".format(self.name))

def main():
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
    print("End")

if __name__ == "__main__":
    main()
