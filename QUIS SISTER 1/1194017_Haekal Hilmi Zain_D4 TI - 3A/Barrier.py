from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

minuman = ['thai tea', 'mixue', 'janjiw', 'boba', 'josu']
finish_line = Barrier(len(minuman))
result = []

def runner():
    name = minuman.pop()
    sleep(randrange(2, 10))
    result.append(name)
    print('%s Sudah siap: %s \n' % (name, ctime()))
    finish_line.wait()


def finisher(result):
    for idx, i in enumerate(result):
        print(str(idx+1) + " Selamat menikmati "+ i)


def main():
    threads = []
    print('Memulai membikin minuman')
    for i in range(len(minuman)):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Minuman Selesai\n')
    print(finisher(result))

if __name__ == "__main__":
    main()