class Kutya:
    def __init__(self, nev, fajta, eletkor):
        self.nev = nev
        self.fajta = fajta
        self.eletkor = int(eletkor)


def kutya_lista():
    kutyak = []
    print('Add meg rendre a kutyák adatait\nHavalamelyiket üresen hagyod, az adatbekérés befejeződik!')
    ssz = 1
    while True:
        print(f'{ssz}. kutya adatai:')
        n = input(f'\tkutya neve:     ')
        if len(n) == 0: break
        f = input(f'\tkutya fajtája:  ')
        if len(f) == 0: break
        k = input(f'\tkutya életkora: ')
        if len(k) == 0: break
        kutyak.append(Kutya(n, f, k))
        ssz += 1
    return kutyak


def vizslak_szam(kutya_lista):
    c = 0
    for k in kutya_lista:
        if k.fajta.lower() == 'vizsla':
            c += 1
    return c


def legoregebb_fajtaja(kutya_lista):
    maxi = 0
    for i in range(1, len(kutya_lista)):
        if kutya_lista[i].eletkor > kutya_lista[maxi].eletkor:
            maxi = i
    return kutya_lista[maxi].fajta


def osszes_T_fajta(kutya_lista, ker_fajta):
    print(f'Az összes {ker_fajta} kutya neve:')
    for k in kutya_lista:
        if k.fajta.lower() == ker_fajta.lower():
            print(f'\t{k.nev}')