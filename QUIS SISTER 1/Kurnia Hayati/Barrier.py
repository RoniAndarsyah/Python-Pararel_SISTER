from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

student = 5
finish_line = Barrier(student)
students = ['fanny', 'devita', 'inggarini']

def siswa():
    name = students.pop() #untuk menghasilkan data satu persatu 
    sleep(randrange(2, 5))
    print('%s submit at: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('Mulai kuis')
    for i in range(student):
        threads.append(Thread(target=siswa))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Batas Akhir pengerjaan kuis!')

if _name_ == "_main_":
    main()