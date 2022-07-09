import multiprocessing
import time

def pungsi():
    print ('Start')
    time.sleep(0.1)
    print ('Finish')

if __name__ == '__main__':
    p = multiprocessing.Process(target=pungsi)
    print ('BEFORE:', p, p.is_alive())
    
    p.start()
    print ('DURING:', p, p.is_alive())
    
    p.terminate()
    print ('TERMINATED:', p, p.is_alive())

    p.join()
    print ('JOINED:', p, p.is_alive())