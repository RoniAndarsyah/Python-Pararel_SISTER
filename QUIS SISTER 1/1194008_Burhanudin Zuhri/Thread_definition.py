import time
from threading import Thread

def campur(i):
    print ("Proses mencampurkan pupuk %d" % i)
    time.sleep(2)
    print (" Mencampurkan pupuk selesai dalam %d" % i)

for i in range(10):
    t = Thread(target=campur, args=(i,))
    t.start()
    