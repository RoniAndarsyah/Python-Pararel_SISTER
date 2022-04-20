from datetime import timedelta, datetime
from time import sleep

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def rear(self):
        return self.items[0]
    def front(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def open(self):
        return self.items

def antrian():
    endtime = datetime.now() + timedelta(seconds = 2)
    tanda='n'
    m = Queue()
    cad = Queue()
    inputan = int(input('Masukan berapa orang yang ingin antri = '))
    for i in range(inputan):
        nama = input('Masukan nama costumer ke %i = '%(i+1))
        m.enqueue(nama)
        cad.enqueue(nama)

    print("Estimasi Jam Pelayanan Customer")
    while not m.isEmpty():
        if not m.isEmpty():
            if tanda=='n':
                print(m.dequeue(),'akan dilayani pada :',datetime.now())
                tanda='y'
            else:
                print(m.dequeue(),'akan dilayani pada :',endtime)
                endtime = endtime + timedelta(seconds = 2)

    tanda='n'
    print("=======================Antrian======================")
    while not cad.isEmpty():
        if not cad.isEmpty():
            if tanda==0:
                print(cad.dequeue(),'sedang dilayani')
                tanda=1
            else:
                sleep(2)
                print(cad.dequeue(),'sedang dilayani')

    if cad.isEmpty():
            print('===============Antrian Kosong==================')
            antrian()

antrian()
            