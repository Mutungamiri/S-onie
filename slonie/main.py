""" 
Zadanie: Słonie
Sposób uruchomienia: python main.py < plik.in
Autor: Mateusz Perdek
"""
def main():
    
    # wczytanie liczby słoni 
    liczba_sloni = int(input())
    
    # wczytanie wag
    temp = input().split()
    wagi = [int(waga) for waga in temp]
    minimalna_waga = min(wagi)

    # wczytanie permutacji początkowej
    temp = input().split()
    permutacja_pierwotna = [int(pier) - 1 for pier in temp]

    # przypisanie miejsc docelowych
    temp = input().split()
    permutacja_temp = [int(tem) - 1 for tem in temp]
    permutacja_docelowa = [0] * liczba_sloni
    for i in range(liczba_sloni):
         numer = permutacja_temp[i]
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

if __name__ == "__main__":
    main()
