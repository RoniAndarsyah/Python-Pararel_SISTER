import threading
import time

def Bersepeda():
    time.sleep(3)
    print('Bersepeda di pagi hari')

def Memancing():
    time.sleep(4)
    print('Memancing di sore hari')

def Belajar():
    time.sleep(5)
    print('Belajar di malam hari')


t1 = threading.Thread(target=Bersepeda, args=())
t2 = threading.Thread(target=Memancing, args=())
t3 = threading.Thread(target=Belajar, args=())

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
