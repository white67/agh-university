import numpy as np

def f1(x):
    return 2 * x**2 + 0.1 * x + 3

def f2(x, y):
    return -2 * x**2 * y + 2 * x * y + 4

def f3(x, y):
    return -5 * x**2 * y + 2 * x * y + 10

gauss_2_points = {
    'points': np.array([-1/np.sqrt(3), 1/np.sqrt(3)]),
    'weights': np.array([1, 1])
}

gauss_3_points = {
    'points': np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)]),
    'weights': np.array([5/9, 8/9, 5/9])
}

def integrate_1d(func, gauss_scheme):
    points = gauss_scheme['points']
    weights = gauss_scheme['weights']
    integral = 0
    for i in range(len(points)):
        integral += weights[i] * func(points[i])
    return integral

def integrate_2d(func, gauss_scheme):
    points = gauss_scheme['points']
    weights = gauss_scheme['weights']
    integral = 0
    for i in range(len(points)):
        for j in range(len(points)):
            integral += weights[i] * weights[j] * func(points[i], points[j])
    return integral

def main():
    scheme_choice = int(input("Wybierz schemat całkowania (2 - 2-punktowy, 3 - 3-punktowy): "))
    
    if scheme_choice == 2:
        gauss_scheme = gauss_2_points
    elif scheme_choice == 3:
        gauss_scheme = gauss_3_points
    else:
        print("Niepoprawny wybór.")
        return

    integral_f1 = integrate_1d(f1, gauss_scheme)
    print(f"Całka funkcji f(x) = 2x^2 + 0.1x + 3 wynosi: {integral_f1}")
    
    integral_f2 = integrate_2d(f2, gauss_scheme)
    print(f"Całka funkcji f(x,y) = -2x^2*y + 2xy + 4 wynosi: {integral_f2}")
    
    integral_f3 = integrate_2d(f3, gauss_scheme)
    print(f"Całka funkcji f(x,y) = -5x^2*y + 2xy + 10 wynosi: {integral_f3}")

if __name__ == "__main__":
    main()