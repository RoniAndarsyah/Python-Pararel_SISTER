import threading


def Memanggil(thread_number):
    return print('memanggil peserta nomor {}'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=Memanggil, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
