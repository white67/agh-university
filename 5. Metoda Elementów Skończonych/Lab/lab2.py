import numpy as np

def calkowanie_gaussa_2d(func, rodzaj='2p'):
    
    if rodzaj == '2p':
        punkty_x = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])  # Punkty wzdłuż osi x
        punkty_y = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])  # Punkty wzdłuż osi y
        wagi = np.array([1, 1])  # wagi dla 2D

    elif rodzaj == '3p':
        punkty_x = np.array([np.sqrt(3 / 5), 0, -np.sqrt(3 / 5)])  # Punkty wzdłuż osi x
        punkty_y = np.array([np.sqrt(3 / 5), 0, -np.sqrt(3 / 5)])  # Punkty wzdłuż osi y
        wagi = np.array([5/9, 8/9, 5/9])  # wagi dla 3-punktowego schematu

    calka = 0.0
    
    # Pętla po wszystkich punktach wzdłuż osi x
    for i in range(len(punkty_x)):
        
        # Pętla po wszystkich punktach wzdłuż osi y
        for j in range(len(punkty_y)):
            
            # Obliczanie wartości funkcji w punktach (x, y)
            func_value = func(punkty_x[i], punkty_y[j])  # Wywołanie funkcji z punktami x i y
            
            # Dodawanie iloczynu wag i wartości funkcji do całki
            calka += wagi[i] * wagi[j] * func_value  # Mnożenie wag i dodawanie do całki

    return calka  # Zwracamy wynik całkowania


if __name__ == "__main__":
    
    def f1(x, y):
        return -2*x**2*y + 2*x*y + 4  # f(x, y) = -2*x^2*y + 2*x*y + 4
    
    def f2(x, y):
        return -5*x**2*y + 2*x*y + 10  # f(x, y) = -5*x^2*y + 2*x*y + 10
    
    wynik_2p = calkowanie_gaussa_2d(f1, rodzaj='2p')
    wynik_3p = calkowanie_gaussa_2d(f2, rodzaj='3p')

    # Wyświetlamy wyniki całkowania
    print(f"Wynik całkowania 2-punktowego: {wynik_2p}")
    print(f"Wynik całkowania 3-punktowego: {wynik_3p}")
