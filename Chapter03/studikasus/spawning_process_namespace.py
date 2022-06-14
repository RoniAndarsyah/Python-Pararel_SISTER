import multiprocessing
from myFunc_studikasus import iniFunction

if __name__ == '__main__':
    for i in range(5):
        process = multiprocessing.Process(target=iniFunction, args=(i,))
        process.start()
        process.join()