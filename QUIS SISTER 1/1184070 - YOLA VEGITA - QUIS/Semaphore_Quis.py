#imprt library
import threading

bounded_semaphore = threading.BoundedSemaphore(100) #penggunaan semaphore

#membuat fungsi
def f1():
    bounded_semaphore.acquire()
    print("%s acquired lock." % (threading.current_thread().name))
    print(bounded_semaphore._value)
    bounded_semaphore.release()
    print("%s released lock." % (threading.current_thread().name))
    print(bounded_semaphore._value)

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f1)
t3 = threading.Thread(target=f1)
t4 = threading.Thread(target=f1)
t5 = threading.Thread(target=f1)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print("Main Thread Exited.", threading.main_thread())