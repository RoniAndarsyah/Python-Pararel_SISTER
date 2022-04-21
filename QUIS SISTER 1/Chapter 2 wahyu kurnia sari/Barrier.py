

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

jumlah_menu = 4
hasilnya = Barrier(jumlah_menu)
menunya = ['BAKSO', 'BATAGOR', 'SIOMAY', 'MIE AYAM', 'KUE BERAS', 'SEBLAK']



def menu():
    cobain = menunya.pop()
    sleep(randrange(2, 3 ))
    print('%s JUGA TERMASUK DALAM MENU \n' % (cobain))
    hasilnya.wait()


def main():
    threads = []
    print('Yang ada disini')
    for i in range(jumlah_menu):
        threads.append(Thread(target=menu))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('okeh beres')

if __name__ == "__main__":
    main()
