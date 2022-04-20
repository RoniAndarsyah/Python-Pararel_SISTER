#import library
import threading
import time
import random


condition = threading.Condition() #membuat variabel condition untuk menampung fitur condition pada threading

#membuat class

class Ngambil():
    #membuat fungsi
    def lalin(self):
        print('Berhenti')

        with condition:
            print('Lampu Merah')
            condition.wait()
            print('Udah hijau, jalan')

    def jalan(self):
        print('nunggu lajur yang lain')

        with condition:
            time = random.randint(25,30)
            waktu = random.randint(5,20)
            print('{} detik lagi'.format(time))
            print('{} detik lagi'.format(waktu))
            condition.notify()

ambil = Ngambil()
lalin = threading.Thread(target=ambil.lalin)
jalan = threading.Thread(target=ambil.jalan)


lalin.start()
jalan.start()

lalin.join()
jalan.join()