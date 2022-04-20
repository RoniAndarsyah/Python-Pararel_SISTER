import threading
from random import randint
import time

def loop_count(thread_number):
    loop_count = randint(1, 20)
    print('Proses {}, Memulai proses looping sebanyak {}'.format(thread_number, loop_count))
    for i in range(loop_count):
        print(i)
    print("selesai")
    return time.sleep(5)


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=loop_count, args=(i,))
        threads.append(t)
        t.start()
        t.join()


if __name__ == "__main__":
    main()
