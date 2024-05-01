# lab7 metody calkowania

import numpy as np
import math

def funkcja_podcalkowa1(x):
    return math.sin(x)

def funkcja_podcalkowa2(x):
    return x**2 + 2*x + 5

def funkcja_podcalkowa3(x):
    return math.exp(x)

def prostokaty(funkcja, a, b, n):
    s = (b - a) / n
    suma = 0
    for i in range(n):
        x = a + i * s
        suma += funkcja(x+s/2)
    wynik = suma * s
    return wynik

def trapezy(funkcja, a, b, n):
    s = (b - a) / n

    suma = 0
    for i in range(n):
        x = a+i*s
        x1 = x + s
        suma += ((x1 - x)/2)*(funkcja(x)+funkcja(x1))
    return suma

def parabole(funkcja, a, b, n):
    suma = 0
    s = (b - a) / n
    for i in range(n):
        x = a + i*s
        fa = funkcja(x)
        fb = funkcja(x+s)
        fab2 = funkcja(x+0.5*s)
        suma += (s/6)*(fa + 4*fab2 + fb)
    return suma

n = 4  # liczba przedziałów

# pierwsza calka
print(f"\nCalka numer 1:\n")

# Wprowadź dane
a = 0.5  # początek przedziału całkowania
b = 2.5  # koniec przedziału całkowania

# Wyświetl dane
print("Funkcja podcałkowa: f(x) = sin(x)")
print("Przedział całkowania: [", a, ",", b, "]")
print("Liczba przedziałów:", n)

# Oblicz i wyświetl wyniki dla każdej metody
wynik_prostokaty = prostokaty(funkcja_podcalkowa1, a, b, n)
wynik_trapezy = trapezy(funkcja_podcalkowa1, a, b, n)
wynik_parabole = parabole(funkcja_podcalkowa1, a, b, n)

print("\nMetoda prostokątów:", wynik_prostokaty)
print("Metoda trapezów:", wynik_trapezy)
print("Metoda parabol:", wynik_parabole)

################################################
# druga calka
print(f"\nCalka numer 2:\n")

# Wprowadź dane
a = 0.5  # początek przedziału całkowania
b = 5  # koniec przedziału całkowania

# Wyświetl dane
print("Funkcja podcałkowa: f(x) = x^2 + 2x + 5")
print("Przedział całkowania: [", a, ",", b, "]")
print("Liczba przedziałów:", n)

# Oblicz i wyświetl wyniki dla każdej metody
wynik_prostokaty = prostokaty(funkcja_podcalkowa2, a, b, n)
wynik_trapezy = trapezy(funkcja_podcalkowa2, a, b, n)
wynik_parabole = parabole(funkcja_podcalkowa2, a, b, n)

print("\nMetoda prostokątów:", wynik_prostokaty)
print("Metoda trapezów:", wynik_trapezy)
print("Metoda parabol:", wynik_parabole)


################################################
# trzecia calka
print(f"\nCalka numer 3:\n")

# Wprowadź dane
a = 0.5  # początek przedziału całkowania
b = 5  # koniec przedziału całkowania

# Wyświetl dane
print("Funkcja podcałkowa: f(x) = exp(x)")
print("Przedział całkowania: [", a, ",", b, "]")
print("Liczba przedziałów:", n)

# Oblicz i wyświetl wyniki dla każdej metody
wynik_prostokaty = prostokaty(funkcja_podcalkowa3, a, b, n)
wynik_trapezy = trapezy(funkcja_podcalkowa3, a, b, n)
wynik_parabole = parabole(funkcja_podcalkowa3, a, b, n)

print("\nMetoda prostokątów:", wynik_prostokaty)
print("Metoda trapezów:", wynik_trapezy)
print("Metoda parabol:", wynik_parabole)


c1_m1 = []
c1_m2 = []
c1_m3 = []
c2_m1 = []
c2_m2 = []
c2_m3 = []
c3_m1 = []
c3_m2 = []
c3_m3 = []
n = []

for i in range(100):
    n.append(i+1)

    c1_m1.append(prostokaty(funkcja_podcalkowa1, a, b, i+1))
    c1_m2.append(trapezy(funkcja_podcalkowa1, a, b, i+1))
    c1_m3.append(parabole(funkcja_podcalkowa1, a, b, i+1))

    c2_m1.append(prostokaty(funkcja_podcalkowa2, a, b, i+1))
    c2_m2.append(trapezy(funkcja_podcalkowa2, a, b, i+1))
    c2_m3.append(parabole(funkcja_podcalkowa2, a, b, i+1))

    c3_m1.append(prostokaty(funkcja_podcalkowa3, a, b, i+1))
    c3_m2.append(trapezy(funkcja_podcalkowa3, a, b, i+1))
    c3_m3.append(parabole(funkcja_podcalkowa3, a, b, i+1))


# Przykładowe dane do zapisania
data = np.array([c1_m1, c1_m2, c1_m3, c2_m1, c2_m2, c2_m3, c3_m1, c3_m2, c3_m3])

# Ścieżka do pliku CSV
csv_file = "dane.csv"

# Zapisanie danych do pliku CSV
np.savetxt(csv_file, data, delimiter=",")
