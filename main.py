import modul as m

kutyamenhely = m.kutya_lista()

# 1. feladat:
print(f'vizslák száma a menhelyen: {m.vizslak_szam(kutyamenhely)}')

# 2. feladat:
print(f'a legöregebb kutya egy {m.legoregebb_fajtaja(kutyamenhely)}')

#3. feladat:
fajta = input('írj be egy kutyafajtát: ')
m.osszes_T_fajta(kutyamenhely, fajta)