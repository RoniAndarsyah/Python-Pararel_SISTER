from random import randrange
import threading
from time import ctime, sleep

hobby = ['Singing','Cooking','Swiming','Drawing','Play Game']

def hobbies(thread_number):
    mine = hobby.pop()
    sleep(randrange(2, 5))
    print('My Hobbies List {}'.format(thread_number))
    return print('%s Merupakan Hobby Saya \n' % (mine)) 


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=hobbies, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()
