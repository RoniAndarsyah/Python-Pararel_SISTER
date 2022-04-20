#studi kasus tentang hp digudang
import threading


def my_hp(thread_number):
    return print('Jumlah Handphone yang ada digudang {} buah'.format(thread_number))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_hp, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
