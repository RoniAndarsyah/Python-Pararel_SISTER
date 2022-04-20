import threading


def my_func(thread_number):
    return print('ayank dimana? {}'.format(thread_number))


def main():
    threads = []
    for i in range(7):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
