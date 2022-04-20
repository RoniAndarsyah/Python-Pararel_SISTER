import threading


def jilbab(thread_number):
    return print('Jumlah Jilbab yang ada ditoko{} pcs'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=jilbab, args=(i,))
        threads.append(t)
        t.start()
        t.join()


if __name__ == "__main__":
    main()
