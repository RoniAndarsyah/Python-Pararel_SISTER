import threading
import time

def lomba():
    print (threading.currentThread().getName()+str('--> memulai lomba \n'))
    
    print (threading.currentThread().getName()+str( '--> lomba selesai \n'))
    time.sleep(2)
    return

def pengumuman():
    print (threading.currentThread().getName()+str('--> mulai pengumuman \n'))
    time.sleep(3)
    print (threading.currentThread().getName()+str( '--> selesai \n'))
    time.sleep(2)
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='lomba', target=lomba)
    t2 = threading.Thread(name='pengumuman', target=pengumuman)
    

    t1.start()
    t2.start()
  
    t1.join()
    t2.join()
   
