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

# Pobranie liczby węzłów w pionie i poziomie
nodes_v = int(input("Podaj liczbę węzłów w pionie: "))
nodes_h = int(input("Podaj liczbę węzłów w poziomie: "))

rozklad.nN = nodes_v * nodes_h  # Aktualizacja liczby węzłów
rozklad.nE = (nodes_v - 1) * (nodes_h - 1)  # Aktualizacja liczby elementów

# Wyznaczanie współrzędnych węzłów siatki
nodes = []
for i in range(nodes_h):
    for j in range(nodes_v):
        # Skalowanie współrzędnych według height i width
        x = i * (width / (nodes_h - 1))
        y = j * (height / (nodes_v - 1))
        nodes.append(Node(x, y))

# Wyświetlanie wszystkich węzłów siatki wraz z ich numeracją
print("\n*Node")
for i in range(rozklad.nN):
    print(f"{i+1} = ({nodes[i].x}, {nodes[i].y})")

# Wyznaczanie elementów siatki (każdy element składa się z 4 węzłów, odpowiednio dobranych przeciwnie do ruchu wskazówek zegara)
elements = []
for i in range(nodes_h - 1):
    for j in range(nodes_v - 1):
        n1 = j * nodes_h + i
        n2 = j * nodes_h + i + 1
        n3 = (j + 1) * nodes_h + i + 1
        n4 = (j + 1) * nodes_h + i
        elements.append(Element(n1, n2, n3, n4))

# Wyświetlanie wszystkich elementów siatki wraz z ich numeracją
print("\n*Element")
for i in range(rozklad.nE):
    print(f"{i+1} = {elements[i].n1+1}, {elements[i].n2+1}, {elements[i].n3+1}, {elements[i].n4+1}")

# Wyświetlenie numerów tylko zewnętrznych węzłów siatki
print("\n*BC")
for i in range(rozklad.nN):
    if nodes[i].x == 0 or nodes[i].x == width or nodes[i].y == 0 or nodes[i].y == height:
        print(f"{i+1}") if i+1 == rozklad.nN else print(f"{i+1}, ", end="")
        