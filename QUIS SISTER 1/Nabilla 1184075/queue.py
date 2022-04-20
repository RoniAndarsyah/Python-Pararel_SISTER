def queue():
    s = []
    return s
def enqueue(s,i):
    s.insert(0,i)
    return s
def dequeue(s):
    return s.pop()
def rear(s):
    return (s[0])
def front(s):
    return (s[len(s)-1])
def size(s):
    return len(s)
def isEmpty(s):
    return s==[]

def No2():
    s = queue()
    k=''
    while True:
        banyak = int(input('Masukan banyak orang yang ingin ada di permainan = '))
        for j in range(banyak):
            orang = input('Masukan nama orang ke %i yang masuk di antrian = '%(j+1))
            enqueue(s,orang)
        s.reverse()
        print('Orang yang berada di Antrian %s'%s)
        s.reverse()
        o = input('Masukan nama orang yang ingin ditemukan = ')
        ditemukan = 't'
        itung = 0
        while ditemukan=='t':
            if o == front(s):
                print('Congrast! Orang ditemukan')
                ditemukan = 'y'
            elif o != front(s):
                masukan = dequeue(s)
                enqueue(s,masukan)
                ditemukan = 't'
                s.reverse()
                print('Looping %i = %s'%((itung+1),s))
                s.reverse()
            itung+=1
            if itung > len(s):
                print('Maaf! Orang yang dimaksud tidak ada')
                ditemukan = 'y'
        print('Total looping yang perlukan adalah',str(itung-1))
        k = input('ingin melanjutkan permainan (y/n) ? ')
        if k != 'y':
            break
        else:
            print('OKE LANJUT')

No2()
    