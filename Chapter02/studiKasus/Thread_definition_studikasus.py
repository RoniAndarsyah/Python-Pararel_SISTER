from random import randint
import threading
import time


def waktu(thread_number):
    count = 0
    while count < 5:
      time.sleep(randint(0,7))
      count += 1
      return print(thread_number, time.ctime(time.time()))


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=waktu, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()