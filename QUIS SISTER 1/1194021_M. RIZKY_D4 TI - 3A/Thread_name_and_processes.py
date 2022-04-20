from threading import Thread
import time
import os
from random import randint

class MyThreadClass (Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name


    def loop_count(self):
        loop_count = randint(1, 20)
        print('Memulai proses looping sebanyak {}'.format(loop_count))
        for i in range(loop_count):
            print(i)
        print("selesai")
        return time.sleep(5)


    def run(self):
        print("ID of process running {}".format(self.name)) #, " is {} \n".format(os.getpid()))
        self.loop_count()


def main():
    from random import randint

    # Thread Creation
    thread1 = MyThreadClass("Looping #1 ")
    thread2 = MyThreadClass("Looping #2 ")


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

    


