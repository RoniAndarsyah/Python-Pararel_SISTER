import threading
import time

def sarapan():
    time.sleep(3)
    print('makan dulu')

def ngopi():
    time.sleep(4)
    print('ngopi dulu')

def belajar():
    time.sleep(5)
    print('belajar dulu')


t1 = threading.Thread(target=sarapan, args=())
t2 = threading.Thread(target=ngopi, args=())
t3 = threading.Thread(target=belajar, args=())

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

# sarapan()
# ngopi()
# belajar()

