# pobranie danych z pliku tekstowego
def read_data(filename):
    x = []
    fx = []
    with open(filename, "r") as lines:
        for line in lines:
            wezly = line.strip().split()
            x.append(float(wezly[0]))
            fx.append(float(wezly[1]))
    return x, fx

def input_data():
    print("Wprowadz punkt: ", end="")
    x = input()
    return float(x)

def pk(x_array, punkt, k):
    wynik = 1
    for i in range(k):
        wynik *= punkt - x_array[i]
    return wynik

def bk(x_array, fx_array, k):
    suma = 0
    for i in range(k+1):
        suma += (fx_array[i]/iloraz(x_array, k, i))
    return suma
                
def iloraz(x_array, k, i):
    wynik = 1
    for j in range(k+1):
        if i != j:
            wynik *= (x_array[i]-x_array[j])
    return wynik

def suma_bkpk(punkt, x_array, fx_array, n):
    suma = 0
    bks = []
    for k in range(1,n):
        suma += bk(x_array, fx_array, k) * pk(x_array, punkt, k)
        bks.append(bk(x_array, fx_array, k))
    return [suma, bks]

def wartosc_wielomianu(b0, p0, punkt, x_array, fx_array):
    n = len(x_array)
    return [(b0*p0 + suma_bkpk(punkt, x_array, fx_array, n)[0]), suma_bkpk(punkt, x_array, fx_array, n)[1]]

########################

x_array, fx_array = read_data("C:\\Users\\kamil\\Documents\\GitHub\\Metody-Numeryczne\\Lab 2. Interpolacja Newtona\\dane.txt")

print(x_array)
print(fx_array)

punkt_input = input_data()

# stałe
p0 = 1
b0 = fx_array[0]

wartosc = wartosc_wielomianu(b0, p0, punkt_input, x_array, fx_array)[0]
bks = wartosc_wielomianu(b0, p0, punkt_input, x_array, fx_array)[1]
    
print(f"\n---------------\nLiczba wezlow: {len(x_array)}")
print(f"Dane:")
for i in range(len(x_array)):
    print(f"x: {x_array[i]}\tf(x): {fx_array[i]}")
print(f"Punkt, w ktorym liczymy wartosc wielomianu: {punkt_input}")
print(f"Wartość wielomianu Newtona w punkcie {punkt_input}: {wartosc}")
for i in range(len(bks)):
    print(f"b{i}: {bks[i]}")
print(f"---------------")