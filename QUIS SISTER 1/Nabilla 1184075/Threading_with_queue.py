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
        banyak = int(input('Dari angka 1-10, seberapa siap kamu? = '))
        for j in range(banyak):
            orang = input('undang teman anda %i yang akan masuk dalam games ini = ' % (j + 1))
            enqueue(s, orang)
        s.reverse()
        print('maka teman anda masuk dalam permainan %s' % s)
        s.reverse()
        o = input('mencari id patner musuh anda = ')
        ditemukan = 't'
        itung = 0
        while ditemukan == 't':
            if o == front(s):
                print('Congrats! id musuh ditemukan')
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
                print('Maaf anda kurang beruntung, Coba lagi ya')
                ditemukan = 'ya'
        print('Total peserta yang di perlukan', str(itung - 5))
        k = input('apakah anda ingin melanjutkan permainannya? (y/t) ? ')
        if k != 'y':
            break
        else:
            print('Semangat, jangan menyerah' )


No2()