#Tugas Studi Kasus 
import threading
import time

def thread_pertama(i):
    time.sleep(5)
    print('Nilai dari '+ str(threading.current_thread().getName())+" adalah: ", i)

def thread_kedua(i):
    time.sleep(6)
    print('Nilai dari '+ str(threading.current_thread().getName())+" adalah: ", i)
    
def thread_ketiga(i):
    time.sleep(7)
    print('Nilai dari '+ str(threading.current_thread().getName())+" adalah: ", i)
    

thread1 = threading.Thread(target=thread_pertama, args=(10,)) # nama default
thread2 = threading.Thread(name='Thread Kedua', target=thread_kedua, args=(20,)) 
thread3 = threading.Thread(name='Thread Ketiga', target=thread_ketiga, args=(30,))

# Running the threads
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
