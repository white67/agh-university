# program oblicza wartosc wielomianu interpolacyjnego Lagrange'a w dowolnym punkcie

# pobranie danych z pliku tekstowego
def read_data(filename):
    data = []
    with open(filename, "r") as lines:
        for line in lines:
            wezly = line.strip().split()
            data.append([float(wezly[0]), float(wezly[1])])
    return data

def input_data():
    print("Wprowadz punkt: ", end="")
    x = input()
    return x

# funkcja obliczajaca pojedyncze wartosci dla poszczegolnych wezlow
def znajdz_wielomiany(punkt, ilosc_wezlow, data):
    wielomiany = []
    for i in range(0, ilosc_wezlow):
        wartosc = 1
        for j in range(0, ilosc_wezlow):
            if i != j:
                wartosc *= ((punkt-data[j][0])/(data[i][0]-data[j][0]))
        wielomiany.append(wartosc)
    return wielomiany

# funkcja obliczajaca sume wielomianow
def znajdz_sume_wielomianow(punkt, ilosc_wezlow, data):
    wielomiany = znajdz_wielomiany(punkt, ilosc_wezlow, data)
    
    wynik = 0
    for i in range(0, len(wielomiany)):
        wynik += data[i][1] * wielomiany[i]
    return wynik

# dzialanie programu
data = read_data("wezly.txt")
wezly_length = len(data)
punkt = float(input_data())
wynik = znajdz_sume_wielomianow(punkt, wezly_length, data)

# wypisanie liczby wezlow
print(f"Liczba wezlow: {wezly_length}")

# wypisanie danych (wezlow interpolacji i wartosci funkcji w wezlach)
print(f"Dane:")
for i in range(wezly_length):
    print(f"x{i} = {data[i][0]} | f(x) = {data[i][1]}")
    
# wypisanie punktu, w ktorym liczymy wartosc wielomianu
print(f"Punkt, w ktorym liczymy wartosc wielomianu = {punkt}")

# wypisanie wartosci wielomianu lagrangea w danym punkcie
print(f"Wartosc wielomiany Lagrange'a w punkcie {punkt} = {wynik}")