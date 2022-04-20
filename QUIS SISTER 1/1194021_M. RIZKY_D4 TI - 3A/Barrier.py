from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

foods = ['cilok', 'seblak', 'batagor', 'bakso', 'mie']
finish_line = Barrier(len(foods))
result = []

def runner():
    name = foods.pop()
    sleep(randrange(2, 10))
    result.append(name)
    print('%s reached the barrier at: %s \n' % (name, ctime()))
    finish_line.wait()


def finisher(result):
    for idx, i in enumerate(result):
        print(str(idx+1) + " di raih oleh "+ i)


def main():
    threads = []
    print('Memulai memasak makanan')
    for i in range(len(foods)):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Memasak Selesai\n')
    print(finisher(result))

if __name__ == "__main__":
    main()