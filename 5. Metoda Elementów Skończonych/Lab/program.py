# stworzenie klasy zawierającej dane symulacji rozkładu
# importowanie bibliotek
import math

PLIK_DANE = "dane.txt"

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Element:
    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        
class Grid:
    def __init__(self, nN, nE, nodes, elements):
        self.nN = nN
        self.nE = nE
        self.nodes = [nodes]
        self.elements = [elements]

class GlobalData:
    def __init__(self, SimulationTime, SimulationStepTime, Conductivity, Alfa, Tot, InitialTemp, Density, SpecificHeat, nN, nE):
        self.SimulationTime = SimulationTime
        self.SimulationStepTime = SimulationStepTime
        self.Conductivity = Conductivity
        self.Alfa = Alfa
        self.Tot = Tot
        self.InitialTemp = InitialTemp
        self.Density = Density
        self.SpecificHeat = SpecificHeat
        self.nN = nN
        self.nE = nE
    
    # funkcja wczytująca dane z pliku PLIK_DANE do obiektu klasy GlobalData
    def read_data(self):
        with open(PLIK_DANE, 'r') as file:
            lines = file.readlines()
            values = [float(line.strip()) for line in lines]
        
        self.SimulationTime = values[0]
        self.SimulationStepTime = values[1]
        self.Conductivity = values[2]
        self.Alfa = values[3]
        self.Tot = values[4]
        self.InitialTemp = values[5]
        self.Density = values[6]
        self.SpecificHeat = values[7]
        self.nN = int(values[8])
        self.nE = int(values[9])
        
    # funkcja wyświetla dane z obiektu klasy GlobalData
    def print_data(self, text):
        print(text)
        print(f"SimulationTime {self.SimulationTime}")
        print(f"SimulationStepTime {self.SimulationStepTime}")
        print(f"Conductivity {self.Conductivity}")
        print(f"Alfa {self.Alfa}")
        print(f"Tot {self.Tot}")
        print(f"InitialTemp {self.InitialTemp}")
        print(f"Density {self.Density}")
        print(f"SpecificHeat {self.SpecificHeat}")
        print(f"Nodes number {self.nN}")
        print(f"Elements number {self.nE}")
        
# stwórz obiekt klasy GlobalData
rozklad = GlobalData(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
rozklad.read_data()

# Pobranie wymiarów siatki
height = float(input("\nPodaj wysokość siatki: "))
width = float(input("Podaj szerokość siatki: "))


# wyznaczanie współrzędnych węzłów siatki
rozmiar_siatki = int(math.sqrt(rozklad.nN))
nodes = []
for i in range(rozmiar_siatki):
    for j in range(rozmiar_siatki):
        # Poprawione skalowanie współrzędnych dla height i width
        x = i * (width / (rozmiar_siatki - 1.0))
        y = j * (height / (rozmiar_siatki - 1.0))
        nodes.append(Node(x, y))

# wyświetl dane
rozklad.print_data("\n")

# wyświetlanie wszystkich węzłów siatki wraz z ich numeracją
print("\n*Node")
for i in range(rozklad.nN):
    print(f"{i+1} = ({nodes[i].x}, {nodes[i].y})")
    
# wyznaczanie elementów siatki (każdy element składa się z 4 węzłów, odpowiednio dobranych przeciwnie do ruchu wskazówek zegara)
elements = []
for j in range(rozmiar_siatki - 1):
    for i in range(rozmiar_siatki - 1):
        n1 = i * rozmiar_siatki + j
        n2 = i * rozmiar_siatki + j + 1
        n3 = (i + 1) * rozmiar_siatki + j + 1
        n4 = (i + 1) * rozmiar_siatki + j
        elements.append(Element(n1, n2, n3, n4))
        
# wyświetlanie wszystkich elementów siatki wraz z ich numeracją
print("\n*Element")
for i in range(rozklad.nE):
    print(f"{i+1} = {elements[i].n1}, {elements[i].n2}, {elements[i].n3}, {elements[i].n4}")
    
# wyświetlenie numerów tylko zewnętrznych węzłów siatki
print("\n*BC")
external_nodes = []
for i in range(rozklad.nN):
    if nodes[i].x == 0 or nodes[i].x == height or nodes[i].y == 0 or nodes[i].y == width:
        external_nodes.append(i+1)
for i in range(len(external_nodes)):
    print(f"{external_nodes[i]}") if i == len(external_nodes) - 1 else print(f"{external_nodes[i]}, ", end="")