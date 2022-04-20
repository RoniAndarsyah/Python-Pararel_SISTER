import threading
import time

def senam_pagi():
    print (threading.currentThread().getName()+str('--> yoga \n'))
    time.sleep(3)
    
def senam_sore():
    print (threading.currentThread().getName()+str('--> lari sore \n'))
    time.sleep(2)
   
    




if __name__ == "__main__":

  
            t1 = threading.Thread(name='senam_pagi', target=senam_pagi)
            t2 = threading.Thread(name='senam_sore', target=senam_sore)

            t1.start()
            t2.start()

            t1.join()
            t2.join()