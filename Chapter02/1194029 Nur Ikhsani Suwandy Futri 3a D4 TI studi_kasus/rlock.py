import threading
import time
import random


class BoxMangga: # kelas boxmangga dengan 2 metode yaitu add dan remove yang 
    #dapat mengakases metode execute
    def __init__(self):
        self.lock = threading.RLock() #pemanggilan rlock dilakukan dengan 
        #metode init pada kelas box mangga
        self.total_items = 0

    def execute(self, value): # untuk menambahkan dan menghapus item 
        #dapat mengakases ke metode execute dengan di atur oleh rlock
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(boxmangga, items):# fungsi dipanggil oleh kedu threads yang memiliki
    # kelas boxmangga dan items agar dapat ditambahkan dan di hapus sbagai parameter.
    print("Banyaknya mangga {} yang ditambahkan \n".format(items))
    while items:
        boxmangga.add()
        time.sleep(1)
        items -= 1
        print("stok buah mangga saat ini -->{} buah \n".format(items))



def remover(boxmangga, items):
    print("banyaknya mangga {} yang di jual \n".format(items))
    while items:
        boxmangga.remove()
        time.sleep(1)
        items -= 1
        print("mangga yang dijual -->{} buah \n".format(items))


def main(): # pada total item dapat ditambah dan dihapus dari kotak kedua akanganya 
    #akan berbeda dan eksekusi akan berakhir ketika kedua metode telah selesai
    items = 2
    box = BoxMangga()

    t1 = threading.Thread(target=adder, \
                          args=(box, random.randint(1,10))) # pada t1 dan t2 telah 
                          #terkait dengan adder da remove
    t2 = threading.Thread(target=remover, \
                          args=(box, random.randint(1,10)))#fungsinya akan aktif 
                          #ketika jumlahitem lebih besar dari nol
    
    t1.start()
    t2.start()


    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
