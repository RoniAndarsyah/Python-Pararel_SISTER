def queue():
    s = []
    return s


def enqueue(s, i):
    s.insert(0, i)
    return s


def dequeue(s):
    return s.pop()


def rear(s):
    return (s[0])


def front(s):
    return (s[len(s) - 1])


def size(s):
    return len(s)


def isEmpty(s):
    return s == []


def No2():
    s = queue()
    k = ''
    while True:
        banyak = int(input('Game valo berhadiah, mau ikut? isi partner tim mulai dari 1 - 9 = '))
        for j in range(banyak):
            orang = input('undang teman kamu %i yang mau masuk dalam games ini = ' % (j + 1))
            enqueue(s, orang)
        s.reverse()
        print('jadi teman kamu masuk dalam permainan %s' % s)
        s.reverse()
        o = input('masukkan nama musuh kamu = ')
        ditemukan = 't'
        itung = 0
        while ditemukan == 't':
            if o == front(s):
                print('Chukkae! musuh ditemukan')
                ditemukan = 'ok'
            elif o != front(s):
                masukan = dequeue(s)
                enqueue(s, masukan)
                ditemukan = 't'
                s.reverse()
                print('Looping %i = %s' % ((itung + 1), s))
                s.reverse()
            itung += 1
            if itung > len(s):
                print('Maaf kamu kurang beruntung, Coba lagi ya')
                ditemukan = 'ya'
        print('Total peserta yang di perlukan', str(itung - 5))
        k = input('apakah kamu mau melanjutkan permainannya? (y/t) ? ')
        if k != 'y':
            break
        else:
            print('Semangat, jangan menyerah' )


No2()