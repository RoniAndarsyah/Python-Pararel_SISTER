import threading


def my_func(thread_number):
    #return print('panggil fungsi N°{}'.format(thread_number))
    return print('Bilangan cacah : {} '.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i, ))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
