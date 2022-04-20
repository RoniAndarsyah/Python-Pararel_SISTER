from threading import Thread
import time
import os


class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Bakso Bakar {}".format(self.name))  # , " is {} \n".format(os.getpid()))


def main():
    from random import randint
    # Thread Creation
    thread1 = MyThreadClass("mantappu ")
    thread2 = MyThreadClass("mantappu")

    # Thread Running
    thread1.start()
    thread2.start()

    # Thread joining
    thread1.join()
    thread2.join()

    # End
    print("Siap Dihidangakan")


if __name__ == "__main__":
    main()




