import threading


def my_func(thread_number):
    return print('panggil fungsi {}'.format(thread_number))
# menampilkan informasi thread


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if _name_ == "_main_":
    main()