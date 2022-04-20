import threading


def function(thread_number):
    return print('function ini di jalankan oleh thread ke {}'.format(thread_number))


def main():
    threads = []
    for i in range(1,11):
        t = threading.Thread(target=function, args=(i,))
        threads.append(t)
        t.start()
        t.join() 

if __name__ == "__main__":
    main()

