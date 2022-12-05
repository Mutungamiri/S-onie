""" 
Zadanie: Słonie
Sposób uruchomienia: np. python main.py slo1.in 
Autor: Mateusz Perdek
"""
import sys

#funkcja służąca do wczytywania kolejnych lini z pliku
def wczytaj(rozmiar, plik):
    temp = []
    linia = plik.readline().split()
    for i in range(rozmiar):
        temp.append(int(linia[i]))
    return temp

def main():
    #wczytanie pliku
    nazwa_pliku = sys.argv[1]
    plik = open(nazwa_pliku, 'r')
    linia = plik.readline().split()
    liczba_sloni = int(linia[0]) #wczytanie liczby słoni (rozmiar zadania)

    #wczytanie wag
    wagi = wczytaj(liczba_sloni, plik) 
    permutacja_pierwotna = []
    permutacja_docelowa = [0] * liczba_sloni
    minimalna_waga = min(wagi)

    #wczytanie permutacji początkowej
    temp = []
    linia = plik.readline().split()
    for i in range(liczba_sloni):
        temp.append(int(linia[i]))
        temp[i] = temp[i] - 1
    permutacja_pierwotna = temp

    #przypisanie miejsc docelowych
    numer = 0
    linia = plik.readline().split()
    for i in range(liczba_sloni):
        numer = int(linia[i])
        numer = numer - 1
        permutacja_docelowa[numer] = permutacja_pierwotna[i]


    zbadany_cykl = [False] * liczba_sloni
    wynik = 0

    #liczenie kosztu w cyklach
    for pocz in range(liczba_sloni):
        if not zbadany_cykl[pocz]:
            minimalna_waga_cykl = float('inf')
            suma = 0
            tmp = pocz
            dlugosc_cyklu = 0
            while True:
                minimalna_waga_cykl = min(minimalna_waga_cykl, wagi[tmp])
                suma += wagi[tmp]
                tmp = permutacja_docelowa[tmp]
                zbadany_cykl[tmp] = True
                dlugosc_cyklu += 1
                if tmp == pocz:
                    break
            wynik += min(suma+(dlugosc_cyklu-2)*minimalna_waga_cykl, suma+minimalna_waga_cykl+(dlugosc_cyklu+1)*minimalna_waga)

    print(wynik)
    plik.close()

if __name__ == "__main__":
    main()
