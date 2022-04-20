import threading
from random import randint

npm=randint(1184001, 1184113)

def kuis(npm):
    return print('Antrian sidang NPM {}'.format(randint(1184001,1184113)))


def main():
    masuk = []
    for i in range(10):
        mulai = threading.Thread(target=kuis, args=(i,))
        masuk.append(mulai)
        mulai.start()
        mulai.join()

if __name__ == "__main__":
    main()
