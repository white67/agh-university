import numpy as np

# Struktura dla elementu, przechowująca wartości Ksi, Eta oraz punkty całkowania
class Elem4:
    def __init__(self, ksi, eta, punkty):
        self.ksi = ksi          # wartości ksi w 4 punktach
        self.eta = eta          # wartości eta w 4 punktach
        self.punkty = punkty    # punkty całkowania

# Funkcja do obliczania pochodnych funkcji kształtu
def oblicz_pochodne_funkcji_ksztaltu(ksi, eta):
    dN_dxi = [
        -(1 / 4) * (1 - eta),
         (1 / 4) * (1 - eta),
         (1 / 4) * (1 + eta),
        -(1 / 4) * (1 + eta)
    ]
    dN_deta = [
        -(1 / 4) * (1 - ksi),
        -(1 / 4) * (1 + ksi),
         (1 / 4) * (1 + ksi),
         (1 / 4) * (1 - ksi)
    ]
    return dN_dxi, dN_deta

# Funkcja do obliczania macierzy Jacobiego, wyznacznika i odwrotności Jacobiego
def oblicz_jakobian(element, x_koord, y_koord):
    for i in range(4):  # Pętla po 4 punktach całkowania
        ksi = element.ksi[i]
        eta = element.eta[i]

        # Uzyskaj pochodne funkcji kształtu
        dN_dxi, dN_deta = oblicz_pochodne_funkcji_ksztaltu(ksi, eta)

        # Oblicz komponenty macierzy Jacobiego
        J = np.zeros((2, 2))
        J[0, 0] = sum(dN_dxi[j] * element.punkty[j][0] for j in range(4))  # dx/deta
        J[0, 1] = sum(dN_dxi[j] * element.punkty[j][1] for j in range(4))  # dy/deta
        J[1, 0] = sum(dN_deta[j] * element.punkty[j][0] for j in range(4))  # dx/dksi
        J[1, 1] = sum(dN_deta[j] * element.punkty[j][1] for j in range(4))  # dy/dksi

        # Oblicz wyznacznik macierzy Jacobiego
        det_J = np.linalg.det(J)

        # Oblicz odwrotność macierzy Jacobiego
        inv_J = np.linalg.inv(J)

        # Wyświetl wyniki dla każdego punktu całkowania
        print(f"######## Punkt całkowania p{i+1}: {element.punkty[i]}:\n")
        print(f"Macierz Jacobiego J = \n{J}")
        print(f"det(J) = {det_J}")
        print(f"Odwrotność Jacobiego J^(-1) = \n{inv_J}\n")

# Wartości punktów całkowania (dla schematu całkowania 2x2)
ksi_wartosci = [-1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3), -1 / np.sqrt(3)]
eta_wartosci = [-1 / np.sqrt(3), -1 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)]

# Współrzędne węzłów
x_koord = [0, 4, 4, 0]  # x1, x2, x3, x4
y_koord = [0, 0, 4, 4]  # y1, y2, y3, y4

punkty_calkowania = []
for i in range(4):
    punkty_calkowania.append([x_koord[i], y_koord[i]])
    
# Zdefiniuj element i współrzędne węzłów
element = Elem4(ksi_wartosci, eta_wartosci, punkty_calkowania)

# Oblicz i wyświetl Jacobian, wyznacznik oraz odwrotność Jacobiana
oblicz_jakobian(element, x_koord, y_koord)
