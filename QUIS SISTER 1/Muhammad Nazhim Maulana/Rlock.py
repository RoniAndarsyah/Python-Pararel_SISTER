import threading
import time
import random


class Tugas:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def eksekusi(self, value):
        with self.lock:
            self.total_items += value

    def tambah(self, ekstra):
        with self.lock:
            self.eksekusi(1 * ekstra)

    def kurang(self, ekstra):
        with self.lock:
            self.eksekusi(-1 * ekstra)

def tambah_tugas(tugas, items):
    print("N° {} tugas yang perlu ditambahkan \n".format(items))
    while items:
        if items > 3:
            tugas.tambah(random.randint(10,20))
        else:
            tugas.tambah(1)
        time.sleep(1)
        items -= 1
        print("Menambahkan tugas -->{} tugas yang perlu ditambahkan \n".format(items))



def kurangi_tugas(tugas, items):
    print("N° {} tugas yang perlu dikurangkan \n".format(items))
    while items:
        if items < 3:
            tugas.kurang(random.randint(10,20))
        else:
            tugas.kurang(1)
        time.sleep(1)
        items -= 1
        print("Mengurangi tugas -->{} tugas yang perlu dikurangkan \n".format(items))


def main():
    waktu_mulai = time.time()

    tugas = Tugas()

    t1 = threading.Thread(target=tambah_tugas, \
                          args=(tugas, random.randint(10,20)))
    t2 = threading.Thread(target=kurangi_tugas, \
                          args=(tugas, random.randint(1,10)))
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()

    # End 
    print("End")

    #Execution Time
    print("--- %s seconds ---" % (time.time() - waktu_mulai))

if __name__ == "__main__":
    main()
