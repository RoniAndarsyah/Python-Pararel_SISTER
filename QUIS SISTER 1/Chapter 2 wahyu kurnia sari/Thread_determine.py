import threading
import time

def function_A():
    print (threading.currentThread().getName()+str('--> tersedia di rumah makan Hj. Maya Pasteur \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> tersedia di rumah makan Hj. Maya Pasteur \n'))
    return

def function_B():
    print (threading.currentThread().getName()+str('--> tersedia di rumah makan saung sunda \n'))
    time.sleep(2)
    print (threading.currentThread().getName()+str( '--> tersedia di rumah makan saung sunda\n'))
    return



if __name__ == "__main__":

    t1 = threading.Thread(name='Makanan Manis', target=function_A)
    t2 = threading.Thread(name='Makanan Pedas', target=function_B)


    t1.start()
    t2.start()


    t1.join()
    t2.join()
