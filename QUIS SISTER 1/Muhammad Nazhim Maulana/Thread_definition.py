import threading


def new_func(thread_number):
    return print('fungsi ini dipanggil oleh N°{}'.format(thread_number))


def main():
    threads = []
    for i in range(20):
        if (i % 5) == 0:
            t = threading.Thread(target=new_func, args=(i,))
            threads.append(t)
            t.start()
            t.join()

if __name__ == "__main__":
    main()