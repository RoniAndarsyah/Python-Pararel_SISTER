import threading
import time

def seminar():
    print (threading.currentThread().getName()+str('--> penjelasan materi \n'))
    time.sleep(5)
    print (threading.currentThread().getName()+str( '--> materi selesai \n'))
    time.sleep(2)
    return

def tanya_jawab():
    print (threading.currentThread().getName()+str('--> mulai sesi tanya jawab \n'))
    time.sleep(5)
    print (threading.currentThread().getName()+str( '--> selesai \n'))
    time.sleep(2)
    return


if __name__ == "__main__":

    t1 = threading.Thread(name='seminar', target=seminar)
    t2 = threading.Thread(name='tanya_jawab', target=tanya_jawab)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

