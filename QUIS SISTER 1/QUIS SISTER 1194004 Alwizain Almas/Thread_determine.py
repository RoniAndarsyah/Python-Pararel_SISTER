import threading
import time

def CuciMobil():
    print (threading.currentThread().getName()+str(' -> Pencucian mobil dimulai \n'))
    time.sleep(5)
    print (threading.currentThread().getName()+str( ' -> Pencucian mobil baru saja selesai \n'))
    return

def CuciMotor():
    print (threading.currentThread().getName()+str(' -> Pencucian motor dimulai \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( ' -> Pencucian motor telah selesai lebih dulu \n'))
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='Cuci Mobil', target=CuciMobil)
    t2 = threading.Thread(name='Cuci Motor', target=CuciMotor)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
