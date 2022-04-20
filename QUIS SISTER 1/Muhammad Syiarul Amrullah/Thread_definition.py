import threading
import random

def GenerateRandomNumber(number):
    listRandom = list()
    for i in range(0,10):
        listRandom.append(random.randint(10,100))
    print("hasil generate random number {} dari operasi ke {}".format(listRandom, number))

def main():
    threads = list()
    for i in range(1,11):
        t = threading.Thread(target=GenerateRandomNumber ,args=(i,)) 
        threads.append(t) 
        t.start()
        t.join()

if __name__ == '__main__':
    main()
