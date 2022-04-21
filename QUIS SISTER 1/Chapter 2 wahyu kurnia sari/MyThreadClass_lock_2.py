import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()


class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the Lock
        threadLock.acquire()
        print("---> " + self.name + \
              " Pendistribusian motor matic sesuai di regional Jawa Barat " \
              + str(os.getpid()) + "\n")
        threadLock.release()
        time.sleep(self.duration)
        print("---> " + self.name + " Pendistribusian di regional III\n")
        # Release the Lock


def main():
    start_time = time.time()

    # Thread Creation
    thread1 = MyThreadClass("Bandung#1 ", randint(1, 8))
    thread2 = MyThreadClass("Subang#2 ", randint(1, 8))
    thread3 = MyThreadClass("Bekasi#3 ", randint(1, 8))
    thread4 = MyThreadClass("Bogor#4 ", randint(1, 8))
    thread5 = MyThreadClass("Tangerang#5 ", randint(1, 8))
    thread6 = MyThreadClass("Tasikmalaya#6 ", randint(1, 8))
    thread7 = MyThreadClass("Sumedang#7 ", randint(1, 8))
    thread8 = MyThreadClass("Cianjur#8 ", randint(1, 8))
    thread9 = MyThreadClass("Ciamis#9 ", randint(1, 8))

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Thread joining
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End
    print("End")

    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()




