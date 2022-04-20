import threading


def my_func(thread_number):
    return print('panggil vicky kalo ada perlu {}'.format(thread_number))


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
