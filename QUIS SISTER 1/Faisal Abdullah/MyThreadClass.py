from threading import Thread
import threading
import time
from random import randint





class ThreadClass(Thread):

    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("{} execute ketika: {}".format(threading.current_thread().getName(), time.ctime()))
        time.sleep(self.duration) 
        print("{} lanjut ketika: {}".format(threading.current_thread().getName(), time.ctime()))

def main():
    start_time = time.time()

    t1 = ThreadClass('T-1', randint(1,11))
    t2 = ThreadClass('T-2', randint(1,11))
    t3 = ThreadClass('T-3', randint(1,11))


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print('beres')

    print("diexcecute selama :  %s detik " % (time.time() - start_time))

if __name__ == "__main__":
    main()