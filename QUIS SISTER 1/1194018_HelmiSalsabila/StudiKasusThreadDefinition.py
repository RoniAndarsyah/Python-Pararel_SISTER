import threading
from time import ctime


def __mi__(thread_number):
    return print('Ini adalah Thread Definition N°{} \n Waktu selesai {}'.format(thread_number, ctime()))

def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=__mi__, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()