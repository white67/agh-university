import numpy as np


def wczytaj_macierz(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        n = len(lines)
        A = np.zeros((n, n))
        B = np.zeros(n)
        for i in range(n):
            row = lines[i].split()
            for j in range(n):
                A[i][j] = float(row[j])
            B[i] = float(row[n])
        return A, B


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


def print_wektor(wektor, x):
    for i in range(len(wektor)):
        print(f"{x}{i}: {wektor[i]}")


def czy_macierz_dominujaca(matrix):
    n = len(matrix)
    war1 = True
    war2 = 0
    for i in range(n):
        lewo = abs(matrix[i][i])
        prawo = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if lewo < prawo:
            war1 = False
        if lewo > prawo:
            war2 += 1
    return True if war1 == True and war2 > 0 else False


def metoda_jacobbiego(A, B, iteracje):
    n = len(A)
    # wektor x wypelniony zerami
    x = np.zeros(n)
    L = np.zeros((n,n))
    U = np.zeros((n,n))

    # rozkład na macierze L, U i D
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = A[i][j]
            elif i < j:
                U[i][j] = A[i][j]

    # macierz L+U
    L_plus_U = L + U

    # macierz D odwrotna
    D_odwrotne = np.diag(1 / np.diag(A))

    # rownanie numer 7
    for i in range(iteracje):
        x = np.dot(D_odwrotne, B - np.dot(L_plus_U, x))

    return x


def metoda_jacobbiego2(A, B, max_iteracje, e):
    iteracje = 0
    n = len(A)
    # wektor x wypelniony zerami
    x = np.zeros(n)
    L_plus_U = A - np.diag(np.diag(A))

    # macierz D odwrotna
    D_odwrotne = np.diag(1 / np.diag(A))

    # rownanie numer 7
    for _ in range(max_iteracje):
        iteracje += 1
        x_new = np.dot(D_odwrotne, B - np.dot(L_plus_U, x))
        if np.linalg.norm(x_new - x) < e:
            break
        x = x_new
    return x, iteracje


# rozwiazanie metoda gaussa
def metoda_gaussa(A, B):
    return np.linalg.solve(A, B)


def absolute_error(x1, x2):
    return np.linalg.norm(x1 - x2)


def print_macierze(L_plus_U, D_inv):
    printMatrix(L_plus_U, "\nMacierz L + U")
    printMatrix(D_inv, "\nMacierz D^-1")


def main():
    # 1. pobieranie danych z pliku
    file_name = "lab6.txt"
    iteracje = int(input("Wpisz liczbe iteracji: "))
    A, B = wczytaj_macierz(file_name)

    # 2. wypisanie macierzy rozszerzonej
    printMatrix(np.column_stack((A, B)), "\nMacierz A (Rozszerzona)")

    # 2.1 wypisanie czy macierz diagonalnie dominujaca
    if czy_macierz_dominujaca(A):
        print("\nMacierz A jest diagonalnie dominujaca.")
    else:
        print("\nMacierz A nie jest diagonalnie dominujaca.")
        return

    # 3. wypisanie macierzy l+u oraz d^-1
    L_plus_U = A - np.diag(np.diag(A))
    D_inv = np.diag(1 / np.diag(A))
    print_macierze(L_plus_U, D_inv)

    # 4. właściwa implementacja
    jacobi_x = metoda_jacobbiego(A, B, iteracje)
    print(f"\nMetoda Jacobbiego ({iteracje} iteracji)")
    print_wektor(jacobi_x, "x")

    gauss_x = metoda_gaussa(A, B)
    print("\nRozwiazanie metoda Gaussa:")
    print_wektor(gauss_x, "gx")

    # 5. obliczanie błędy bezwzględnego dla każdego x
    error = absolute_error(jacobi_x, gauss_x)
    print("\nBlad bezwzgledny:", error)

    # warunek stopu
    epsilon_values = [0.001, 0.000001]
    max_iteracje = 5000
    for epsilon in epsilon_values:
        jacobi2_x, jacobi2_iteracje = metoda_jacobbiego2(A, B, max_iteracje, epsilon)
        print(f"\nRozwiazanie po {jacobi2_iteracje} gdzie epsilon = {epsilon}")
        print_wektor(jacobi2_x, "x")


if __name__ == "__main__":
    main()