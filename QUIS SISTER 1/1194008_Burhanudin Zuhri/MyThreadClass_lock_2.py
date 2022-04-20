import threading
import time

kendaraan = threading.Lock()

def Mobil(kendaraan):
    kendaraan.acquire()
    print('Mobil sedang melewati terowongan')
    time.sleep(1)
    print('Mobil sudah melewati terowongan')

def Motor(kendaraan):
    print('Motor sedang melewati terowongan')
    kendaraan.release()
    time.sleep(1)
    print('Motor sudah melewati terowongan')


t1 = threading.Thread(target=Mobil, args=(kendaraan, ))
t2 = threading.Thread(target=Motor, args=(kendaraan, ))

t1.start()
t2.start()

t1.join()
t2.join()