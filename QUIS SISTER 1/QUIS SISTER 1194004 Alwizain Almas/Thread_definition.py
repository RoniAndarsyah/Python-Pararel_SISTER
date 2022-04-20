import time
from threading import Thread

def myfunc(i):
    print ("Peserta yang berangkat dengan nomor urut %d" % i)
    time.sleep(5)
    print ("Peserta yang kembali dengan nomor urut %d" % i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()