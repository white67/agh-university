import sys

# funkcja wczytująca pliki składające się na macierz
def read_data(filename1, filename2):
    x = []
    with open(filename1, "r") as lines:
        i = 0
        for line in lines:
            x.append([])
            numbers = line.strip().split()
            for num in numbers:
                x[i].append(float(num))
            i += 1
            
    with open(filename2, "r") as lines:
        i = 0
        for line in lines:
            num = line.strip()
            x[i].append(float(num))
            i += 1
            
    return x

# funkcja wypisująca macierz na ekran
def printMatrix(matrix):
    for line in matrix:
        for i in range(len(line)):
            if abs(line[i]) <= 0.000001:
                print("0.0", "\t", end="")
            else:
                print(round(line[i],2), "\t", end="")
        print("\n", end="")
        
def pierwszy_etap(macierz):
    
    kolumny = list(range(len(macierz)))
    
    for i in range(len(macierz)):
        for j in range(len(macierz)-1):
            
            j += i + 1
            
            # Sprawdzenie, czy nie wykracza poza macierz
            if j < len(macierz):
                
                # znajdź największą wartość w danej kolumnie
                max_value = abs(macierz[i][i])
                max_index = i
                for k in range(i, len(macierz)):
                    if abs(macierz[k][i]) > max_value:
                        max_value = abs(macierz[k][i])
                        max_index = k
                
                # Zamień kolumnę z maksymalną wartością z aktualną kolumną
                macierz[i], macierz[max_index] = macierz[max_index], macierz[i]
                kolumny[i], kolumny[max_index] = kolumny[max_index], kolumny[i]
    
                # Sprawdzenie, czy element na przekątnej nie jest zerem
                # if macierz[i][i] == 0:
                #     print("\n### 0 na przekątnej!!!")
                #     sys.exit(1)
                    
                # obliczanie mnożnika
                wartosc_mnoznika = macierz[j][i]/macierz[i][i]
                
                # iteracja po kolumnach macierzy
                for k in range(len(macierz[j])):
                    
                    # odejmij wiersze aby powstały zera
                    macierz[j][k] = macierz[j][k] - wartosc_mnoznika * macierz[i][k]

        # print(f"\n### {i}.\n")
    
    return macierz, kolumny

def drugi_etap(macierz, kolumny):
    
    # stworzenie listy przechowującej wyniki obliczeń
    wyniki = [0] * len(macierz)
    
    # iteracja w dół (od ostatniego wiersza) x_k
    for i in range(len(macierz)-1, -1, -1):
        # pobranie wartości na ostatniej prawej kolumnie, b_i = macierz[i][-1]
        wyniki[i] = macierz[i][-1]

        # suma od i+1 do n, a_ik = macierz[i][j], x_k = wyniki[j]
        for j in range(i+1, len(macierz)):
            wyniki[i] -= macierz[i][j] * wyniki[j]

        # a_ii = macierz[i][i]
        wyniki[i] = wyniki[i] / macierz[i][i]
    
    # Wypisanie wyników
    for i, x in zip(kolumny, wyniki):
        print(f"x{i}: {x}")
    
    return wyniki
        

def wypisz_wyniki(wyniki):
    # Wypisz wyniki po kolei
    for i, val in enumerate(wyniki):
        print(f"x{i}: {val}")
        

# Funkcja główna
if __name__ == "__main__":
    dane = read_data("C:\\Users\\kamil\\Documents\\GitHub\\agh-university\\4. Metody Numeryczne\\Lab 4. Eliminacja Gaussa - pivoting\\A2.txt", "C:\\Users\\kamil\\Documents\\GitHub\\agh-university\\4. Metody Numeryczne\\Lab 4. Eliminacja Gaussa - pivoting\\B2.txt")

    # 1) macierz przed obliczeniami
    print("1) Macierz przed obliczeniami:")
    printMatrix(dane)

    # 2) Macierz po pierwszym etapie obliczeń
    print("\n\n2) Macierz po pierwszym etapie obliczeń")
    macierz_po_pierwszym_etapie, kolumny = pierwszy_etap(dane)
    printMatrix(macierz_po_pierwszym_etapie)

    # 3) Rozwiązanie układu równań (x0 - xn)
    print("\n\n3) Rozwiązanie układu równań (x0 - xn)")
    wyniki = drugi_etap(macierz_po_pierwszym_etapie, kolumny)

    # 4) Wypisz uporządkowane wyniki
    print("\n\n4) Uporządkowane wyniki (x0 - xn):")
    wypisz_wyniki(wyniki)