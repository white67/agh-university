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
    for i in range(len(macierz)):
        
        for j in range(len(macierz)-1):
            
            j += i + 1
            
            # Sprawdzenie, czy nie wykracza poza macierz
            if j < len(macierz):
                
                # ustawienie najwiekszej liczby w kolumnie na diagonali
                wartosc_first = macierz[i][i]
                swap = macierz[i]
                g_index = i
                for g in range(i, len(macierz)):
                    if macierz[g][i] > wartosc_first:
                        swap = macierz[g]
                        wartosc_first = macierz[g][i]
                        g_index = g
                # swap wiersze
                macierz[g_index] = macierz[i]
                macierz[i] = swap
    
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
    
    return macierz

def drugi_etap(macierz):
    
    # stworzenie listy przechowującej wyniki obliczeń
    wyniki = []
    for i in range(len(macierz)):
        wyniki.append(0)
    
    # iteracja w dół (od ostatniego wiersza) x_k
    for i in range(len(macierz)-1, -1, -1):
        # pobranie wartości na ostatniej prawej kolumnie, b_i = macierz[i][-1]
        wyniki[i] = macierz[i][-1]

        # suma od i+1 do n, a_ik = macierz[i][j], x_k = wyniki[j]
        for j in range(i+1, len(macierz)):
            wyniki[i] -= macierz[i][j] * wyniki[j]

        # a_ii = macierz[i][i]
        wyniki[i] = wyniki[i] / macierz[i][i]
    
    for line in enumerate(wyniki):
        print(f"x{line[0]}: {line[1]}")

dane = read_data("C:\\Users\\kamil\\Documents\\GitHub\\agh-university\\4. Metody Numeryczne\\Lab 4. Eliminacja Gaussa - pivoting\\A2.txt", "C:\\Users\\kamil\\Documents\\GitHub\\agh-university\\4. Metody Numeryczne\\Lab 4. Eliminacja Gaussa - pivoting\\B2.txt")

# 1) macierz przed obliczeniami
print("1) Macierz przed obliczeniami:")
printMatrix(dane)

# 2) Macierz po pierwszym etapie obliczeń
print("\n\n2) Macierz po pierwszym etapie obliczeń")
printMatrix(pierwszy_etap(dane))

# 3)
print("\n\n3) Rozwiązanie układu równań (x0 - xn)")
drugi_etap(dane)