from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

promo_shopee = 1
finish_line = Barrier(promo_shopee)
runners = ['Shopee Mantul Sale']

def runner():
    name = runners.pop()
    sleep(randrange(2, 4))
    print('%s Mulai tanggal: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('Jangan Lupa')
    for i in range(promo_shopee):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Ayo Download Aplikasi Shopee Sekarang!!!')

if __name__ == "__main__":
    main()
