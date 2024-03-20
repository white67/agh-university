def read_data(filename):
    x = []
    with open(filename, "r") as lines:
        i = 0
        for line in lines:
            x.append([])
            numbers = line.strip().split()
            for num in numbers:
                x[i].append(float(num))
            i += 1
    return x

def printMatrix(matrix):
    for line in matrix:
        for i in range(len(line)):
            print(line[i], "\t", end="")
        print("\n", end="")
        
def pierwszy_etap(macierz):
    for i in range(len(macierz)):
        
        for j in range(len(macierz)-1):
            
            j += i + 1
            
            if j < len(macierz):
                    
                # oblicz mnoznik
                wartosc_mnoznika = macierz[j][i]/macierz[i][i]
                
                print(f"\nwartosc_mnoznika: {wartosc_mnoznika}")
                
                for k in range(len(macierz[j])):
                    
                    # odejmij wiersze
                    macierz[j][k] = macierz[j][k] - wartosc_mnoznika * macierz[i][k]
                
                printMatrix(macierz)

        # print(f"\n### {i}.\n")
        printMatrix(macierz)

def drugi_etap(macierz):
    xn = macierz[-1][-1]/macierz[-1][-2]
    n = len(macierz)-1
    
    def xi(macierz, i, n):
        def suma(k, n):
            wynik = 0
            for i in range(k, n):
                wynik += macierz[i][k]*xi(macierz, k, n)
            print(f"wynik: {wynik}")
            return wynik

        return (macierz[i][-1] - suma(i+1, n))/macierz[i][i]
    
    x0 = xi(macierz, 0, n)
    
    print(f"\nx0: {x0}")
    print(f"\nxn: {xn}")
    print(f"\nx0 - xn: {x0 - xn}")

dane = read_data("C:\\Users\\kamil\\Documents\\GitHub\\Metody-Numeryczne\\Lab 3. Eliminacja Gaussa\\dane.txt")


printMatrix(dane)

pierwszy_etap(dane)

drugi_etap(dane)