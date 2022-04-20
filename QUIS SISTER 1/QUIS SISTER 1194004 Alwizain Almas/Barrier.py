from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_persons = 3
finish = Barrier(num_persons)
persons = ['Si A', 'Si B', 'Si C']

def editing():
    name = persons.pop()
    sleep(randrange(2, 5))
    print('%s Mulai mengedit pada: %s ' % (name, ctime()))
    finish.wait()
    print('%s Selesai mengedit pada: %s ' % (name, ctime()))

def main():
    threads = []
    print('Editing dimulai!')
    for i in range(num_persons):
        threads.append(Thread(target=editing))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Editing selesai!')

if __name__ == "__main__":
    main()