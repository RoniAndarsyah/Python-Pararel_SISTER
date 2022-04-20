import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition() 
# Variabel condition digunakan untuk memungkinkan satu atau lebih thread untuk menunggu hingga diberitahukan oleh thread lain.


class Pembeli(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def beli(self):

        with condition: # membungkus / enkapsulasi proses dengan metode dari variabel condition.

            if len(items) == 0:
                logging.info('Tidak ada makanan yang dapat dibeli')
                condition.wait()

            items.pop() # menghapus 1 item pada index
            logging.info('Kamu membeli 1 item makanan')

            condition.notify() # membangunkan thread yg menunggu variabel condition (jika ada)
                                # / memberi notif ke thread lain bahwa untuk sementara waktu proses disini sudah selesai

    def run(self):
        for i in range(20):
            time.sleep(2) # jeda waktu untuk membeli
            self.beli()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def jual(self):

        with condition: # membungkus / enkapsulasi proses dengan metode dari variabel condition.

            if len(items) == 10:
                logging.info('Di etalase terdapat {} item. Tidak cukup tempat. Produksi berhenti sementara'.format(len(items)))
                condition.wait() # jika kondisinya sudah memenuhi tidak langsung berhenti, namun menunggu beberapa saat untuk proses thread lain

            items.append(1) # akan bertambah 1 setiap prosesnya
            logging.info('Terdapat {} item makanan saat ini'.format(len(items))) # mengembalikan item yang dihapus

            condition.notify() # membangunkan thread yg menunggu variabel condition (jika ada)
                                # / memberi notif ke thread lain bahwa untuk sementara waktu proses disini sudah selesai

    def run(self):
        for i in range(20):
            time.sleep(0.5) # jeda waktu produksi
            self.jual()


def main():
    pembeli = Penjual(name='Penjual') # (name) menginisialisasikan class Penjual dengan nama "penjual" agar dapat terbaca pada output
    penjual = Pembeli(name='Pembeli') # (name) menginisialisasikan class Pembeli dengan nama "pembeli" agar dapat terbaca pada output

    penjual.start()
    pembeli.start()

    penjual.join()
    pembeli.join()


if __name__ == "__main__":
    main()
