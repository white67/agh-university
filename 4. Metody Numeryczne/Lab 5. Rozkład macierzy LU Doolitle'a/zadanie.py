# funkcja wczytująca pliki składające się na macierz
def read_data(filename1, single):
    x = []
    if single:
        with open(filename1, "r") as lines:
            for line in lines:
                x.append(float(line.strip()))
    else:
        with open(filename1, "r") as lines:
            i = 0
            for line in lines:
                x.append([])
                numbers = line.strip().split()
                for num in numbers:
                    x[i].append(float(num))
                i += 1
            
    return x


def newEmptyMatrix(x):
    a = []
    for i in range(x):
        a.append([])
        for j in range(x):
            a[i].append(0)
    return a


def newEmptyMatrixLinear(x):
    a = []
    for i in range(x):
        a.append(0)
    return a
    
    
# funkcja wypisująca macierz na ekran
def printMatrix(matrix, text):
    print(text)
    for line in matrix:
        for i in range(len(line)):
            if abs(line[i]) <= 0.000001:
                print("0.0", "\t", end="")
            else:
                print(round(line[i],2), "\t", end="")
        print("\n", end="")


def printMatrixSingle(matrix, text):
    print(text)
    for line in matrix:
        if abs(line) <= 0.000001:
            print("0.0", "\t", end="")
        else:
            print(round(line,2), "\t", end="")
        print("\n", end="")


def printMatrixRozszerzone(m1, m2, text):
    for i in range(len(m1)):
        m1[i].append(m2[i])
    printMatrix(m1, text)


def rozklad_LU(A):
    n = len(A)
    L = newEmptyMatrix(n)
    U = newEmptyMatrix(n)
    
    # przypisanie 1 na przekatnych
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = 1
    
    # obliczanie macierzy L i U
    for i in range(n):
        
        for k in range(i, n):
            U[i][k] = A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
    
        for k in range(i + 1, n):
            if U[i][i] != 0:
                L[k][i] = (A[k][i] - sum(L[k][j] * U[j][i] for j in range(i))) / U[i][i]
            else:
                L[k][i] = 0
        
    return L, U


def obliczY(L, b):
    n = len(L)
    y = newEmptyMatrixLinear(n)
    
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    return y


def obliczX(U, y):
    n = len(U)
    x = newEmptyMatrixLinear(n)
    
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            print("\n############# ZERO NA PRZEKATNEJ")
            x[i] = 0
        else:
            x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    
    return x
    
    
def rozwiazanie(A, b):
    # printMatrix(A, "\nMACIERZ A")
    L, U = rozklad_LU(macierzA)
    printMatrix(U, "\nMACIERZ U")
    printMatrix(L, "\nMACIERZ L")
    y = obliczY(L, b)
    printMatrixSingle(y, "\nMACIERZ Y")
    x = obliczX(U, y)
    printMatrixSingle(x, "\nMACIERZ X")
    
# main
macierzA = read_data("A2.txt", False)
macierzB = read_data("B2.txt", True)
printMatrixRozszerzone(macierzA, macierzB, "Macierz rozszerzona")
rozwiazanie(macierzA, macierzB)